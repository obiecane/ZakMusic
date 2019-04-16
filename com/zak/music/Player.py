import logging
import threading

import pygame
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtSignal, QObject

from com.zak.music.LocalMusic import Music

pygame.mixer.init()


class Player(QObject):
    # 加载中信号
    signal_loading = pyqtSignal()
    # 开始播放信号
    signal_start_play = pyqtSignal(Music)
    # 播放完毕
    signal_music_over = pyqtSignal(Music)

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
        self.__music_list = []
        self.__curr_index = -1
        self.__set_pos = -1
        self.__status = Player.STATUS_INIT
        self._cond = threading.Condition
        self._curr_music = None
        self.__listen_end_timer = QTimer()
        self.__listen_end_timer.timeout.connect(self.__th_listen_end)  # 计时结束调用__th_listen_end方法
        self.__listen_end_timer.start(500)  # 设置计时间隔为500ms并启动


    def play(self, music):
        if not isinstance(music, Music):
            return
        if self._curr_music is not None:
            try:
                self._curr_music.signal_load_over.disconnect()
                self._curr_music.signal_loading.disconnect()
            except Exception as e:
                logging.debug(e)
        self._curr_music = music
        self.__set_pos = -1
        if music in self.__music_list:
            self.__curr_index = self.__music_list.index(music)
        else:
            self.__curr_index += 1
            self.__music_list.insert(self.__curr_index, music)

        music.signal_loading.connect(self.slot_loading)
        music.signal_load_over.connect(self.slot_load_over)

        uri = self._curr_music.get_uri()
        if not isinstance(uri, str):
            return
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
            # TODO 可能文件损坏 或者因为没有版权
            # TODO 发送信号cant play
            logging.info(e)
            pass

    def _do_load(self):
        uri = self._curr_music.get_uri()
        pygame.mixer.music.load(uri)
        self.__status = Player.STATUS_READY

    def stop(self):
        try:
            pygame.mixer.music.stop()
            self.__status = Player.STATUS_OVER
        except Exception as e:
            logging.info(e)
            print(e)

    def slot_loading(self):
        self.signal_loading.emit()
        pass

    def slot_load_over(self):
        self._do_load()
        self._do_play()

    def pause(self):
        pygame.mixer.music.pause()
        self.__status = Player.STATUS_PAUSE

    def unpause(self):
        pygame.mixer.music.unpause()
        self.__status = Player.STATUS_PLAYING

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
            self.__set_pos = pos
            if self.__status == Player.STATUS_PLAYING:
                pygame.mixer.music.load(self._curr_music.get_uri())
                pygame.mixer.music.play(start=(pos / 1000))
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
            print(over_music.get_name() + "   播放完毕")

    def add_music_list(self, music_or_list):
        if isinstance(music_or_list, Music):
            self.__music_list.append(music_or_list)
        elif isinstance(music_or_list, list) \
                or isinstance(music_or_list, set):
            for m in music_or_list:
                if isinstance(m, Music) and m not in self.__music_list:
                    self.__music_list.append(m)

    # TODO 增加歌词显示
    # TODO 增加异步加载网络数据
    # TODO 完善加载中动画
    # TODO 增加本地搜索
    # TODO 保持localListWidget中的数据和player中维护的播放列表一致
