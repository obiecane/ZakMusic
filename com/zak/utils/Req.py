import json

import requests


class ReqUtils:
    # 搜索音乐 / 专辑 / 歌词 / 歌单 / MV / 用户 / 歌手 / 电台搜索
    # 请求URL: https: // api.itooi.cn / music / netease / search
    # 请求示例: https: // api.itooi.cn / music / netease / search?key = 579621905 & s = 我喜欢上你内心时的活动 & type = song & limit = 100 & offset = 0
    # 参数说明    是否必须        说明          默认值
    # key         √           请求秘钥，   QQ群号579621905
    # s           ×           搜索关键词   详细见下面说明
    # id          ×            歌曲id
    # type        ×           搜索类型        默认为song
    # limit       ×           请求数量        默认为100
    # offset      ×               分页      默认第1页
    # 音乐搜索: type = song
    # 歌手搜索: type = singer
    # 专辑搜索: type = album
    # 歌单搜索: type = list
    # 视频搜索: type = video
    # 电台搜索: type = radio
    # 用户搜索: type = user
    # 歌词搜索: type = lrc
    _NETEASE_BASE_SEARCH = "https://api.itooi.cn/music/netease/search?key=579621905"

    @staticmethod
    def search_music(music_tag):
        ReqUtils._search_music_by_name(music_tag)
        pass

    @staticmethod
    def _search_music_by_name(music_name):
        url = ReqUtils._NETEASE_BASE_SEARCH + "&s=" + music_name
        print(url)
        get_result = requests.get(url)
        loads = json.loads(get_result.content.decode())
        print(loads)
        pass
