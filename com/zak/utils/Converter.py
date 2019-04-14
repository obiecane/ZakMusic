import logging

from com.zak.music.NetMusic import NetMusic


# 转换器, 其他格式的数据转换成Music对象
class Converter:

    @staticmethod
    def itooi_music(json):
        logging.debug("json转music:%s" % json)
        music = NetMusic()
        music.set_id(json['id'])
        music.set_name(json['name'])
        music.set_singer(json['singer'])
        music.set_pic(json['pic'])
        music.set_lrc(json['lrc'])
        music.set_length(json['time'])
        music.set_uri(json['url'])
        return music
        pass
