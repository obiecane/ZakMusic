import logging
import threading

from PyQt5.QtCore import QObject, pyqtSignal

from com.zak.utils.ReqUtils import ReqUtils


class Searcher(QObject):
    __rLock = threading.RLock()
    # 搜索成功事件
    signal_search_success = pyqtSignal(list)
    # 搜索失败
    signal_search_fail = pyqtSignal()
    # 开始搜索
    signal_search_begin = pyqtSignal()

    def __init__(self):
        super().__init__()
        # 子线程是否发出信号的标志
        # 只有当子线程持有的f和flag相同时才发射信号
        # 这样就能保证只有最近一次搜索才会发出信号
        self.__flag = 0

    def search_music(self, music_tag: str):
        self.signal_search_begin.emit()
        f = self._incr_flag()
        thread = threading.Thread(target=self.__do_search, args=(music_tag, f))
        thread.start()
        pass

    def __do_search(self, music_tag: str, f: int):
        try:
            music_list = ReqUtils.search_music(music_tag)
            _f = self._get_flag()
            if _f == f:
                self.signal_search_success.emit(music_list)
        except Exception as e:
            logging.info(e)
            _f = self._get_flag()
            if _f == f:
                self.signal_search_fail.emit()

    # 加锁访问
    def _get_flag(self):
        Searcher.__rLock.acquire()
        _flag = self.__flag
        Searcher.__rLock.release()
        return _flag

    def _incr_flag(self):
        Searcher.__rLock.acquire()
        self.__flag += 1
        _flag = self.__flag
        Searcher.__rLock.release()
        return _flag
