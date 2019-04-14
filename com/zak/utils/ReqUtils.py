import imghdr
import json
import logging
import os

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
        logging.debug("搜索 %s" % music_tag)
        return ReqUtils._search_music_by_name(music_tag)

    @staticmethod
    def _search_music_by_name(music_name):
        url = ReqUtils._NETEASE_BASE_SEARCH + "&s=" + music_name
        logging.debug("搜索 url:%s" % url)
        get_result = requests.get(url)
        json_result = json.loads(get_result.content.decode())
        logging.debug("搜索结果: %s" % json_result)
        if json_result["code"] == 200:
            return json_result["data"]
        else:
            return []

    @staticmethod
    def download(url, filename, override=False):
        if not isinstance(filename, str):
            return
        dir_name = os.path.dirname(filename)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        if override or not os.path.exists(filename):
            logging.debug("开始下载[%s] [url:%s]" % (filename, url))
            result = requests.get(url)
            with open(filename, "wb") as tmp:
                tmp.write(result.content)
            logging.debug("下载完成[%s]" % filename)
        # 自动判断图片的类型
        img_type = imghdr.what(filename)
        if img_type is not None:
            new_filename = filename[:-4] + "." + img_type
            os.rename(filename, new_filename)
            filename = new_filename
        return filename
