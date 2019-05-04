from PyQt5 import QtWidgets

from com.zak.dao.SettingDao import SettingDao
from com.zak.utils.DBUtils import DBUtils


class MyQMainWindow(QtWidgets.QMainWindow):

    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        volume_slider = self.findChild(QtWidgets.QSlider, "volume_slider")
        SettingDao.set_volume(volume_slider.value())
        player = self.player
        pos = player.get_pos()
        player.pause()
        music = player.curr_music()
        if music is None:
            SettingDao.set_last_music(None)
            SettingDao.set_last_pos(0)
        else:
            SettingDao.set_last_music(music.get_id())
            SettingDao.set_last_pos(pos)
        DBUtils.clear_up()
        event.accept()
        # reply = QtWidgets.QMessageBox.question(self,
        #                                        '本程序',
        #                                        "是否要退出程序？",
        #                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
        #                                        QtWidgets.QMessageBox.No)
        # if reply == QtWidgets.QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()

    def showEvent(self, *args, **kwargs):
        self.__re_tab_width()

    def resizeEvent(self, *args, **kwargs):
        self.__re_tab_width()

    def __re_tab_width(self):
        tabWidget = self.ui.tabWidget
        self_width = self.width()
        tabWidget_width = tabWidget.width()
        if tabWidget_width > self_width:
            tab_width = 180
        else:
            tab_count = tabWidget.count()
            tab_width = int(tabWidget_width / tab_count - 1)
        tabWidget.setStyleSheet("QTabBar::tab{width:%dpx;}" % tab_width)
