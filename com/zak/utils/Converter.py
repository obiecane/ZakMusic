import logging

from com.zak.music.LocalMusic import LocalMusic
from com.zak.music.NetMusic import NetMusic


# 转换器, 其他格式的数据转换成Music对象
class Converter:

    @staticmethod
    def itooi_music(json):
        logging.debug("json转music:%s" % json)
        music = NetMusic()
        music.set_id(json['id'])
        music.set_name(json['name'].replace("/", "-"))
        music.set_singer(json['singer'].replace("/", "-"))
        music.set_pic(json['pic'])
        music.set_lrc(json['lrc'])
        music.set_length(json['time'])
        music.set_uri(json['url'])
        return music
        pass

    # 数据库中查出的数据转LocalMusic
    @staticmethod
    def local_data_local_music(data):
        m = LocalMusic()
        m.set_id(data[1])
        m.set_name(data[2])
        m.set_singer(data[3])
        m.set_length(data[4])
        m.set_uri(data[5])
        m.set_pic(data[7])
        m.set_lrc(data[9])
        return m
