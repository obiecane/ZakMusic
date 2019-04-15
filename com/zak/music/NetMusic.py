import os
import threading

from com.zak.music.LocalMusic import LocalMusic
from com.zak.music.Music import Music
from com.zak.utils.ReqUtils import ReqUtils


# 网络音乐资源, 是本地音乐资源的代理类
class NetMusic(Music):
    def __init__(self):
        super().__init__()
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
        # 本地音乐文件
        self._local_music = None
        self.__pic_path = None
        # 标志
        self.__retrieving = False

    def __download_music(self):
        self.signal_loading.emit()
        ReqUtils.download(self._uri, self.__get_local_music_path())
        ReqUtils.download(self._lrc, self.__get_local_lrc_path())
        self.__pic_path = ReqUtils.download(self._pic, self.__get_local_pic_path())
        # 下载完成后判断大小, 107kb则是无版权的
        size = os.path.getsize(self.__get_local_music_path())
        if size < 500:
            # 转到qq去下载
            qq_search_list = ReqUtils.tencent_search_music("%s %s" % (self._name, self._singer), True)
            if len(qq_search_list) > 0:
                data = qq_search_list[0]
                self._uri = data["url"]
                self._pic = data["pic"]
                self._lrc = data["lrc"]
                ReqUtils.download(self._uri, self.__get_local_music_path(), True)
                ReqUtils.download(self._lrc, self.__get_local_lrc_path(), True)
                self.__pic_path = ReqUtils.download(self._pic, self.__get_local_pic_path(), True)

        # 通知外部已下载完毕, 然后外部就开始播放
        self.__create_local_music()
        self.signal_load_over.emit(self)

    def get_source(self):
        if "netease" in self._uri:
            return 1
        elif "tencent" in self._uri:
            return 2
        else:
            return 0

    def get_uri(self, own=False):
        if own:
            return self._uri
        # 开启子线程, 下载
        if not self.__retrieving:
            self.__retrieving = True
            thread = threading.Thread(target=self.__download_music)
            thread.start()
            return self._uri
        return self._local_music.get_uri()

    def get_length(self):
        if self._local_music is None:
            return self._length
        return self._local_music.get_length()

    def get_id(self):
        if self._local_music is None:
            return self._id
        return self._local_music.get_id()

    def get_name(self):
        if self._local_music is None:
            return self._name
        return self._local_music.get_name()

    def get_singer(self):
        if self._local_music is None:
            return self._singer
        return self._local_music.get_singer()

    def get_lrc(self, own=False):
        if own:
            return self._lrc
        if self._local_music is None:
            return self._lrc
        return self._local_music.get_lrc()

    def get_pic(self, own=False):
        if own:
            return self._pic
        if self._local_music is None:
            return self._pic
        return self._local_music.get_pic()

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

    def __create_local_music(self):
        if self._local_music is None:
            self._local_music = LocalMusic()
            self._local_music.set_id(self._id)
            self._local_music.set_name(self._name)
            self._local_music.set_uri(self.__get_local_music_path())
            self._local_music.set_lrc(self.__get_local_lrc_path())
            self._local_music.set_pic(self.__pic_path)
            self._local_music.set_singer(self._singer)
            self._local_music.set_length(self._length)

    def __get_local_music_path(self):
        return "./music/" + self._singer + "/" + self._name + ".mp3"

    def __get_local_pic_path(self):
        return "./pic/" + self._singer + "/" + self._name + ".jpg"

    def __get_local_lrc_path(self):
        return "./lrc/" + self._singer + "/" + self._name + ".lrc"
