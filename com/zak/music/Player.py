import threading

import pygame
from PyQt5.QtCore import pyqtSignal, QObject

from com.zak.music.LocalMusic import Music

pygame.mixer.init()


class Player(QObject):
    # 加载中信号
    signal_loading = pyqtSignal()
    # 开始播放信号
    signal_start_play = pyqtSignal(Music)

    def __init__(self):
        super().__init__()
        self._cond = threading.Condition
        self._curr_music = None
        self._is_pause = True

    def play(self, music):
        if not isinstance(music, Music):
            return
        if not self._curr_music is None:
            self._curr_music.signal_load_over.disconnect()
            self._curr_music.signal_loading.disconnect()
        self._curr_music = music
        music.signal_loading.connect(self.slot_loading)
        music.signal_load_over.connect(self.slot_load_over)

        uri = self._curr_music.get_uri()
        if not isinstance(uri, str):
            return
        if not uri.startswith("http"):
            self._do_play()

    def _do_play(self):
        name = threading.current_thread().name
        print(name)
        self.signal_start_play.emit(self._curr_music)
        print("发送signal_start_play信号")
        pygame.mixer.music.load(self._curr_music.get_uri())
        pygame.mixer.music.play()
        self._is_pause = False

    def stop(self):
        pygame.mixer.music.stop()

    def slot_loading(self):
        print("signal_loading 信号接收")
        self.signal_loading.emit()
        pass

    def slot_load_over(self):
        print("signal_load_over 信号接收")
        self._do_play()

    def pause(self):
        print("pause")
        pygame.mixer.music.pause()

    def unpause(self):
        print("unpause")
        pygame.mixer.music.unpause()

    def smart_pause(self):
        try:
            busy = pygame.mixer.music.get_busy()
            if busy:
                if not self._is_pause:
                    self.pause()
                    self._is_pause = True
                else:
                    self.unpause()
                    self._is_pause = False
        except Exception as e:
            pass

    def test_signal(self):

        self._do_play()
