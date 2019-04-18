from PyQt5.QtCore import pyqtSignal, QObject


# 定义接口
class Music(QObject):
    signal_loading = pyqtSignal()
    signal_load_over = pyqtSignal(QObject)

    def __init__(self):
        super().__init__()

    def get_uri(self) -> str:
        pass

    def get_length(self):
        pass

    def get_id(self):
        pass

    def get_name(self):
        pass

    def get_singer(self):
        pass

    def get_lrc(self):
        pass

    def get_pic(self):
        pass

    def set_id(self, id_):
        pass

    def set_name(self, name):
        pass

    def set_pic(self, pic):
        pass

    def set_length(self, length: int) -> int:
        pass

    def set_lrc(self, lrc):
        pass

    def set_singer(self, singer):
        pass

    def set_uri(self, uri):
        pass

    def __str__(self):
        return "%s %s %s %d" % (self.get_id(), self.get_name(), self.get_singer(), self.get_length())

    def __hash__(self):
        return hash("name:%s|singer:%s" % (self.get_name(), self.get_singer()))

    def __eq__(self, other):
        if not isinstance(other, Music):
            return False
        if self.get_name() == other.get_name() and self.get_singer() == other.get_singer():
            return True
        return False
