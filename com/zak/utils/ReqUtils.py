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

    _TENCENT_BASE_SEARCH = "https://api.itooi.cn/music/tencent/search?key=579621905"

    # 整合qq和网易云的搜索结果
    @staticmethod
    def search_music(music_tag, exact=False):
        logging.debug("搜索 %s" % music_tag)
        netease_result = ReqUtils.netease_search_music(music_tag, exact)
        tencent_result = ReqUtils.tencent_search_music(music_tag, exact)
        new_result = list()
        tmp = set()
        len_n = len(netease_result)
        len_t = len(tencent_result)
        len_max = max(len_n, len_t)
        for i in range(len_max - 1):
            if i < len_n:
                str_n = "name:%s|singer:%s" % (netease_result[i]["name"], netease_result[i]["singer"])
            else:
                str_n = None

            if i < len_t:
                str_t = "name:%s|singer:%s" % (tencent_result[i]["name"], tencent_result[i]["singer"])
            else:
                str_t = None

            if str_n is not None and str_n not in tmp:
                new_result.append(netease_result[i])
                tmp.add(str_n)
            if str_t is not None and str_t not in tmp:
                new_result.append(tencent_result[i])
                tmp.add(str_t)

        # tmp_ = set()
        # new_result_ = list()
        # for v in netease_result:
        #     tmp_.add("name:%s|singer:%s" % (v["name"], v["singer"]))
        #     new_result_.append(v)
        #
        # for v in tencent_result:
        #     str_ = "name:%s|singer:%s" % (v["name"], v["singer"])
        #     if str_ not in tmp_:
        #         new_result_.append(v)
        #
        # # TODO 去重
        # print(len(new_result))
        # print(len(new_result_))
        return new_result

    @staticmethod
    def netease_search_music(music_tag, exact=False):
        return ReqUtils._search_music_by_name(music_tag, ReqUtils._NETEASE_BASE_SEARCH, exact)
        pass

    @staticmethod
    def tencent_search_music(music_tag, exact=False):
        return ReqUtils._search_music_by_name(music_tag, ReqUtils._TENCENT_BASE_SEARCH, exact)

    @staticmethod
    def _search_music_by_name(music_name, base_search, exact=False):
        url = base_search + "&s=" + music_name
        if exact:
            url += "&type=song"
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
            size = os.path.getsize(filename)
            print(size)
            # 自动判断图片的类型
            img_type = imghdr.what(filename)
            if img_type is not None:
                new_filename = filename[:-4] + "." + img_type
                try:
                    os.rename(filename, new_filename)
                except Exception as e:
                    pass
                filename = new_filename
        return filename
