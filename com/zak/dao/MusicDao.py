import logging

from com.zak.music.NetMusic import NetMusic
from com.zak.utils.Converter import Converter
from com.zak.utils.DBUtils import DBUtils


class MusicDao:
    # 本地音乐表
    # id 本地id，整数，自增长
    # music_id 音乐id
    # name 歌名
    # singer 歌手
    # length 时长
    # music_local_path 歌曲本地文件路径
    # music_net_url 歌曲网络下载url
    # pic_local_path 封面本地文件路径
    # pic_net_url 封面网络下载url
    # lrc_local_path 歌词本地文件路径
    # lrc_net_url 歌词网络下载url
    # source 来源 1 网易云 2 腾讯
    # sort 排序字段

    @staticmethod
    def save(net_music: NetMusic):
        by_name = MusicDao.get_by_music_id(net_music.get_id())
        if by_name is not None:
            return

        conn = DBUtils.get_connect()
        cursor = conn.cursor()
        sql = "insert into music values (null, '%s', '%s', '%s', %d, '%s', '%s', '%s', '%s', '%s', '%s', %d, %d )" % (
            net_music.get_id(),
            net_music.get_name(),
            net_music.get_singer(),
            net_music.get_length(),
            net_music.get_uri(),
            net_music.get_uri(True),
            net_music.get_pic(),
            net_music.get_pic(True),
            net_music.get_lrc(),
            net_music.get_lrc(True),
            net_music.get_source(),
            0
        )
        try:
            cursor.execute(sql)
        except Exception as e:
            logging.debug(e)
        cursor.close()
        conn.commit()

    @staticmethod
    def get_all(cook=True):
        cursor = DBUtils.get_cursor()
        cursor.execute("select * from music")
        values = cursor.fetchall()
        cursor.close()
        # 转换成music对象
        if cook:
            musics = []
            for v in values:
                m = Converter.local_data_local_music(v)
                musics.append(m)
            return musics
        return values

    @staticmethod
    def get_by_name(name, cook=True):
        value = DBUtils.get_by_single("music", "name", name)
        # 转换成music对象
        if cook and value is not None:
            m = Converter.local_data_local_music(value)
            return m
        return value

    @staticmethod
    def get_by_music_id(music_id: str, cook=True):
        value = DBUtils.get_by_single("music", "music_id", music_id)
        # 转换成music对象
        if cook and value is not None:
            m = Converter.local_data_local_music(value)
            return m
        return value

    @staticmethod
    def get_by_id(id_: int, cook=True):
        value = DBUtils.get_by_single("music", "id", id_)
        # 转换成music对象
        if cook and value is not None:
            m = Converter.local_data_local_music(value)
            return m
        return value
