from mutagen.mp3 import MP3


class MusicUtils:

    @staticmethod
    def get_length(file_name: str):
        music = MP3(file_name)
        return music.info.length
        pass
