import logging
import threading

import pygame
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtSignal, QObject

from com.zak.core.LocalMusic import Music

pygame.mixer.init()


class Player(QObject):
    # 加载中信号
    signal_loading = pyqtSignal()
    # 开始播放信号
    signal_start_play = pyqtSignal(Music)
    # 播放完毕
    signal_music_over = pyqtSignal(Music)
    # 暂停
    signal_music_pause = pyqtSignal()
    # 继续
    signal_music_unpause = pyqtSignal()

    # 初始状态
    STATUS_INIT = 0
    # 就绪(已加载， 但是未播放)
    STATUS_READY = 1
    # 播放中
    STATUS_PLAYING = 2
    # 暂停
    STATUS_PAUSE = 3
    # 播放完毕
    STATUS_OVER = 4

    def __init__(self):
        super().__init__()
        # 播放列表
        self.__music_list = []  # 播放列表
        self.__curr_index = -1  # 当前播放的歌在播放列表中的位置
        self.__set_pos = -1  # 当前歌曲播放位置
        self.__status = Player.STATUS_INIT  # 播放器的状态
        self._cond = threading.Condition  # 线程锁
        self._curr_music = None  # 当前播放的音乐
        self.__listen_end_timer = QTimer()  # 定时器
        self.__listen_end_timer.timeout.connect(self.__th_listen_end)  # 计时结束调用__th_listen_end方法
        self.__listen_end_timer.start(500)  # 设置计时间隔为500ms并启动

    # 播放给定的歌曲
    def play(self, music: Music):
        if self._curr_music is not None:
            self.__disconnect_curr_music()
        self._curr_music = music
        self.__set_pos = -1
        self.__connect_curr_music()

        uri = self._curr_music.get_uri()
        if not uri.startswith("http"):
            self._do_load()
            self._do_play()

    # 真正开始播放的方法
    # loop重复播放的次数
    # 例如 _do_play(loop=5) 意味着被载入的音乐将会立即开始播放 1 次并且再重复 5 次，共 6 次。
    # 如果 loops = -1，则表示无限重复播放。
    # pos 开始播放的位置，单位为ms
    def _do_play(self, loop=0, pos=0.0):
        try:
            # pygame.mixer.music.play需要的参数是秒
            pos_ = pos / 1000
            pygame.mixer.music.play(loop, pos_)
            self.__status = Player.STATUS_PLAYING
            self.signal_start_play.emit(self._curr_music)
        except Exception as e:
            # 可能文件损坏 或者因为没有版权
            logging.info(e)  # 记录日志
            pass

    def _do_load(self):
        # 歌曲被从硬盘删除将抛出异常
        try:
            uri = self._curr_music.get_uri()
            pygame.mixer.music.load(uri)
            self.__status = Player.STATUS_READY
        except Exception as e:
            logging.info(e)

    def stop(self):
        try:
            pygame.mixer.music.stop()
            self.__status = Player.STATUS_OVER
        except Exception as e:
            logging.info(e)

    def slot_loading(self):
        self.signal_loading.emit()
        pass

    def slot_load_over(self, music: Music):
        if music in self.__music_list:
            self.__curr_index = self.__music_list.index(music)
        else:
            self.__curr_index += 1
            self.__music_list.insert(self.__curr_index, music)
        self._do_load()
        self._do_play()

    def pause(self):
        pygame.mixer.music.pause()
        self.__status = Player.STATUS_PAUSE
        self.signal_music_pause.emit()

    def unpause(self):
        pygame.mixer.music.unpause()
        self.__status = Player.STATUS_PLAYING
        self.signal_music_unpause.emit()

    def set_volume(self, v):
        pygame.mixer.music.set_volume(v / 99)

    def smart_pause(self):
        try:
            if self.__status == Player.STATUS_PAUSE:
                self.unpause()
            elif self.__status == Player.STATUS_PLAYING:
                self.pause()
            elif self.__status == Player.STATUS_READY:
                self._do_play(pos=(self.__set_pos if self.__set_pos > -1 else 0))
                self.signal_music_unpause.emit()
        except Exception as e:
            logging.info(e)

    def get_pos(self):
        pos = pygame.mixer.music.get_pos()
        offset = self.__set_pos if self.__set_pos > -1 else 0
        return pos + offset

    def load(self, music: Music):
        if music in self.__music_list:
            self.__curr_index = self.__music_list.index(music)
        else:
            self.__curr_index += 1
            self.__music_list.insert(self.__curr_index, music)
        self._curr_music = music
        self._do_load()

    def set_pos(self, pos: int):
        try:
            if self.__status == Player.STATUS_INIT \
                    or self.__status == Player.STATUS_OVER:
                return
            if self.__status == Player.STATUS_PLAYING \
                    or self.__status == Player.STATUS_PAUSE \
                    or (self.__status == Player.STATUS_READY and self.__set_pos != -1):
                self.__status = Player.STATUS_PLAYING
                pygame.mixer.music.load(self._curr_music.get_uri())
                pygame.mixer.music.play(start=(pos / 1000))
            self.__set_pos = pos
        except Exception as e:
            logging.info(e)

    def curr_music(self):
        return self._curr_music

    def is_play(self):
        return self.__status == Player.STATUS_PLAYING

    # 监听是否播放完毕
    def __th_listen_end(self):
        if self.__status == Player.STATUS_PLAYING \
                and pygame.mixer.music.get_busy() == 0 \
                and len(self.__music_list) > 0:
            over_music = self._curr_music
            self.__curr_index += 1
            if self.__curr_index >= len(self.__music_list):
                self.__curr_index = 0
            self._curr_music = self.__music_list[self.__curr_index]
            self.__set_pos = -1
            self._do_load()
            self._do_play()
            self.signal_music_over.emit(over_music)
            logging.debug("%s   播放完毕" % over_music.get_name())

    # 设置播放列表
    def add_music_list(self, music_or_list):
        if isinstance(music_or_list, Music):
            self.__music_list.append(music_or_list)
        elif isinstance(music_or_list, list) \
                or isinstance(music_or_list, set):
            for m in music_or_list:
                if isinstance(m, Music) and m not in self.__music_list:
                    self.__music_list.append(m)

    # 增加歌曲到歌单
    # 如果歌单已有， 返回-1， 否则返回在list中的index
    # def add_to_music_list(self, music: Music) -> int:
    #     try:
    #         i = self.__music_list.index(music)
    #         return -1
    #     except Exception as e:
    #         self.__music_list.append(music)
    #         return self.__music_list.index(music)

    # 获取播放列表
    def get_music_list(self):
        return self.__music_list

    # 上一曲
    def play_prev(self):
        if len(self.__music_list) <= 0:
            return
        self.__disconnect_curr_music()
        self.__set_pos = -1
        self.__curr_index = self.__curr_index - 1 if self.__curr_index > 0 else len(self.__music_list)
        self._curr_music = self.__music_list[self.__curr_index]
        self._do_load()
        self._do_play()
        pass

    def play_next(self):
        if len(self.__music_list) <= 0:
            return
        self.__disconnect_curr_music()
        self.__set_pos = -1
        self.__curr_index = self.__curr_index + 1 if self.__curr_index < len(self.__music_list) - 1 else 0
        self._curr_music = self.__music_list[self.__curr_index]
        self._do_load()
        self._do_play()
        pass

    # 断开与当前音乐的信号监听
    def __disconnect_curr_music(self):
        try:
            self._curr_music.signal_load_over.disconnect()
            self._curr_music.signal_loading.disconnect()
        except Exception as e:
            logging.debug(e)

    def __connect_curr_music(self):
        if self._curr_music is None:
            return
        self._curr_music.signal_loading.connect(self.slot_loading)
        self._curr_music.signal_load_over.connect(self.slot_load_over)

    # TODO 增加本地搜索
    # TODO 增加歌词显示
