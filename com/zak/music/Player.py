import threading
import time

import pygame

from com.zak.music.LocalMusic import Music

pygame.mixer.init()


class Player:

    def __init__(self):
        self._cond = threading.Condition
        self._thread = threading.Thread(target=self._do_play)
        self._curr_music = None
        self._thread.start()

    def play(self, music):
        if not isinstance(music, Music):
            return
        self._curr_music = music
        pygame.mixer.music.load(self._curr_music.get_uri())

    def _do_play(self):
        while True:
            try:
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.play()
                    time.sleep(60 * 60 * 24)
            except Exception as e:
                pass

    def stop(self):
        pygame.mixer.music.stop()
