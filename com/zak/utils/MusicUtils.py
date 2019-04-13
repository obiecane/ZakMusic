import time

import pygame
from mutagen.mp3 import MP3


class MusicUtils:

    @staticmethod
    def play(file_name):
        pygame.mixer.init()

        length = MusicUtils.get_length(file_name)
        pygame.mixer.music.load(file_name)

        pygame.mixer.music.play()
        time.sleep(length)
        pygame.mixer.music.stop()

    @staticmethod
    def get_length(file_name):
        music = MP3(file_name)
        return music.info.length
        pass
