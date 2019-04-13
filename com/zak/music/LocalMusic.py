from com.zak.music.Music import Music
from com.zak.utils.MusicUtils import MusicUtils


class LocalMusic(Music):
    def __init__(self):
        # id
        self._id = None
        # 演唱者
        self._singer = None
        # 歌名
        self._name = None
        # 资源地址
        self._uri = None
        # 封面地址
        self._pic = None
        # 歌词地址
        self._lrc = None
        # 时长(秒)
        self._length = None

    def get_uri(self):
        return self._uri

    def get_length(self):
        if self._uri is not None:
            return MusicUtils.get_length(self._uri)
        return self._length

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_singer(self):
        return self._singer

    def get_lrc(self):
        return self._lrc

    def get_pic(self):
        return self._pic

    def set_id(self, id_):
        self._id = id_

    def set_name(self, name):
        self._name = name

    def set_pic(self, pic):
        self._pic = pic

    def set_length(self, length):
        self._length = length

    def set_lrc(self, lrc):
        self._lrc = lrc

    def set_singer(self, singer):
        self._singer = singer

    def set_uri(self, uri):
        self._uri = uri
