from com.zak.music.NetMusic import NetMusic


# 转换器, 其他格式的数据转换成Music对象
class Converter:

    @staticmethod
    def itooi_music(json):
        data = json['data']
        music = NetMusic()
        music.set_id(data['id'])
        music.set_name(data['name'])
        music.set_singer(data['singer'])
        music.set_pic(data['pic'])
        music.set_lrc('lrc')
        music.set_length(data['time'])
        music.set_uri(data['url'])
        return music
        pass
