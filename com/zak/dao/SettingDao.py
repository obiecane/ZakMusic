import logging

from com.zak.utils.DBUtils import DBUtils


class SettingDao:

    @staticmethod
    def set_volume(value: int):
        SettingDao.__update("volume", value)
        pass

    @staticmethod
    def set_last_pos(last_pos: int):
        SettingDao.__update("last_pos", last_pos)
        pass

    @staticmethod
    def set_last_music(music_id):
        SettingDao.__update("last_music", music_id)

    @staticmethod
    def get_volume():
        v = SettingDao.__get("volume")
        if v is None:
            return 0
        else:
            return int(v)

    @staticmethod
    def get_last_music():
        v = SettingDao.__get("last_music")
        return v

    @staticmethod
    def get_last_pos():
        v = SettingDao.__get("last_pos")
        if v is None:
            return 0
        else:
            return int(v)

    @staticmethod
    def __get(name):
        v_ = DBUtils.get_by_single("setting", "name", name)
        try:
            v = v_[2]
            return v
        except Exception as e:
            logging.info(e)
            return None

    @staticmethod
    def __update(name, value):
        conn = DBUtils.get_connect()
        if value is None:
            sql = "update setting set value = null where name = '%s'" % name
        else:
            sql = "update setting set value = '%s' where name = '%s'" % (str(value), name)
        conn.execute(sql)
        conn.commit()
