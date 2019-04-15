import sqlite3


class DBUtils:
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
    __music_table_sql = "create table music (" \
                        "id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                        "music_id varchar(255), " \
                        "name varchar(100), " \
                        "singer varchar(100), " \
                        "length INTEGER, " \
                        "music_local_path varchar(255), " \
                        "music_net_url varchar(255), " \
                        "pic_local_path varchar(255), " \
                        "pic_net_url varchar(255), " \
                        "lrc_local_path varchar(255), " \
                        "lrc_net_url varchar(255), " \
                        "source INTEGER, " \
                        "sort INTEGER DEFAULT 0)"

    # 软件设置记录表
    # id id
    # name 设置项名称
    # value 设置项的值
    __setting_table_sql = "create table setting (" \
                          "id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                          "name varchar(255), " \
                          "value varchar(255) )"

    @staticmethod
    def get_connect():
        conn = sqlite3.connect("lyt_music.db")
        return conn

    @staticmethod
    def get_cursor():
        return DBUtils.get_connect().cursor()

    @staticmethod
    def create_table(self):
        pass

    @staticmethod
    def init_tables():
        conn = DBUtils.get_connect()
        try:
            conn.execute(DBUtils.__music_table_sql)
        except Exception as e:
            print(e)
            pass
        try:
            conn.execute(DBUtils.__setting_table_sql)
            # 音量
            DBUtils.exec("insert into setting values (NULL, 'volume', '80')")
            # 软件退出时播放的歌的id
            DBUtils.exec("insert into setting values (NULL, 'last_music', NULL)")
            # 软件退出时播放的位置
            DBUtils.exec("insert into setting values (NULL, 'last_pos', NULL)")
        except Exception as e:
            print(e)
            pass

    @staticmethod
    def exec(sql: str, param=None):
        conn = DBUtils.get_connect()
        if param is None:
            param = []
        cursor = conn.cursor()
        cursor.execute(sql, param)
        fetchall = cursor.fetchall()
        cursor.close()
        conn.commit()
        return fetchall

    @staticmethod
    def get_by_single(table: str, column: str, value):
        cursor = DBUtils.get_cursor()
        cursor.execute("select * from %s where %s = ?" % (table, column), (value,))
        value = cursor.fetchone()
        cursor.close()
        return value
