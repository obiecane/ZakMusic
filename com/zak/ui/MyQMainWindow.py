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
        player.pause()
        music = player.curr_music()
        pos = player.get_pos()
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