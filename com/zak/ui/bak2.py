# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QTimer
from PyQt5.QtGui import QMovie

from com.zak.core.Music import Music
from com.zak.core.Player import Player
from com.zak.dao.MusicDao import MusicDao
from com.zak.dao.SettingDao import SettingDao
from com.zak.ui.MyQSlider import MyQSlider
from com.zak.utils.Converter import Converter
from com.zak.utils.ReqUtils import ReqUtils
from com.zak.utils.TimeUtils import TimeUtils


# Form implementation generated from reading ui file 'LYTMusic.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


class Ui_MainWindow(QObject):
    __QSlider_Qss = "  \
             QSlider::add-page:Horizontal\
             {     \
                background-color: rgb(87, 97, 106);\
                height:4px;\
             }\
             QSlider::sub-page:Horizontal \
            {\
                background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(231,80,229, 255), stop:1 rgba(7,208,255, 255));\
                height:4px;\
             }\
            QSlider::groove:Horizontal \
            {\
                background:transparent;\
                height:6px;\
            }\
            QSlider::handle:Horizontal \
            {\
                height: 0px;\
                width:12px;\
                border-image: url(./res/ic_slider_thumb.png);\
                margin: -3 0px; \
            }\
            "

    __QListWidget_Qss = "QListWidget{border:0px solid black;}"

    __QListWidget_Item_Qss = "QListWidgetItem{border-bottom: 1px solid gray;}"

    def __init__(self):
        super().__init__()
        self._player = Player()
        self._music_timer = QTimer()
        self._music_timer.timeout.connect(self.__refresh_music_progress)  # 计时结束调用operate()方法
        self._music_timer.start(800)  # 设置计时间隔并启动

    def setupUi(self, MainWindow):
        MainWindow.player = self._player
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(380, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.input_search = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.input_search.setFont(font)
        self.input_search.setInputMask("")
        self.input_search.setText("")
        self.input_search.setObjectName("input_search")
        self.verticalLayout_2.addWidget(self.input_search)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.volume_label = QtWidgets.QLabel(self.centralwidget)
        self.volume_label.setObjectName("volume_label")
        self.horizontalLayout_4.addWidget(self.volume_label)
        self.volume_slider = MyQSlider(self.centralwidget)
        self.volume_slider.setTracking(True)
        self.volume_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_slider.setInvertedControls(False)
        self.volume_slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.volume_slider.setObjectName("volume_slider")
        self.horizontalLayout_4.addWidget(self.volume_slider)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.page)
        self.tabWidget.setStyleSheet("QTabBar::tab{width:180px;}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.tab)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.local_list_widget = QtWidgets.QListWidget(self.page_3)
        self.local_list_widget.setStyleSheet(Ui_MainWindow.__QListWidget_Qss)
        self.local_list_widget.setObjectName("local_list_widget")
        self.verticalLayout_6.addWidget(self.local_list_widget)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget_2.addWidget(self.page_4)
        self.verticalLayout_5.addWidget(self.stackedWidget_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.tab_2)
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.net_list_widget = QtWidgets.QListWidget(self.page_5)
        self.net_list_widget.setStyleSheet(Ui_MainWindow.__QListWidget_Qss)
        self.net_list_widget.setObjectName("net_list_widget")
        self.verticalLayout_7.addWidget(self.net_list_widget)
        self.stackedWidget_3.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.stackedWidget_3.addWidget(self.page_6)
        self.verticalLayout_4.addWidget(self.stackedWidget_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pic_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.pic_label.sizePolicy().hasHeightForWidth())
        self.pic_label.setSizePolicy(sizePolicy)
        self.pic_label.setMinimumSize(QtCore.QSize(50, 50))
        self.pic_label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pic_label.setAutoFillBackground(False)
        self.pic_label.setText("")
        self.pic_label.setObjectName("pic_label")
        self.horizontalLayout.addWidget(self.pic_label)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.song_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.song_label.setFont(font)
        self.song_label.setStyleSheet("QLabel{color: black}")
        self.song_label.setObjectName("song_label")
        self.verticalLayout.addWidget(self.song_label)
        self.singer_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.singer_label.setFont(font)
        self.singer_label.setStyleSheet("QLabel {color:gray}")
        self.singer_label.setObjectName("singer_label")
        self.verticalLayout.addWidget(self.singer_label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.curr_music_time = QtWidgets.QLabel(self.centralwidget)
        self.curr_music_time.setObjectName("curr_music_time")
        self.horizontalLayout_3.addWidget(self.curr_music_time)
        self.music_progress = MyQSlider(self.centralwidget)
        self.music_progress.setOrientation(QtCore.Qt.Horizontal)
        self.music_progress.setObjectName("music_progress")
        self.horizontalLayout_3.addWidget(self.music_progress)
        self.full_music_time = QtWidgets.QLabel(self.centralwidget)
        self.full_music_time.setObjectName("full_music_time")
        self.horizontalLayout_3.addWidget(self.full_music_time)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.mc_prev = QtWidgets.QPushButton(self.centralwidget)
        self.mc_prev.setMinimumSize(QtCore.QSize(0, 38))
        self.mc_prev.setObjectName("mc_prev")
        self.horizontalLayout_2.addWidget(self.mc_prev)
        self.mc_play_pause = QtWidgets.QPushButton(self.centralwidget)
        self.mc_play_pause.setMinimumSize(QtCore.QSize(50, 50))
        self.mc_play_pause.setObjectName("mc_play_pause")
        self.horizontalLayout_2.addWidget(self.mc_play_pause)
        self.mc_next = QtWidgets.QPushButton(self.centralwidget)
        self.mc_next.setMinimumSize(QtCore.QSize(0, 38))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.mc_next.setFont(font)
        self.mc_next.setObjectName("mc_next")
        self.horizontalLayout_2.addWidget(self.mc_next)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.volume_slider.hitSliderClicked.connect(self.refresh_volume)
        self.volume_slider.setStyleSheet(Ui_MainWindow.__QSlider_Qss)
        self.music_progress.setStyleSheet(Ui_MainWindow.__QSlider_Qss)
        # self.volume_slider.setStyleSheet("QSlider::sub-page: horizontal{ background:rgb(255, 85, 127)}")
        self.volume_slider.valueChanged.connect(self.refresh_volume)
        self.input_search.returnPressed.connect(self.search)
        self.net_list_widget.doubleClicked.connect(self.net_list_widget_double_click)
        self.local_list_widget.doubleClicked.connect(self.local_list_widget_double_click)
        self._player.signal_start_play.connect(self.slot_music_start_play)
        self.mc_play_pause.clicked.connect(self._player.smart_pause)
        self.mc_next.clicked.connect(self._player.play_next)
        self.mc_prev.clicked.connect(self._player.play_prev)
        self.music_progress.hitSliderClicked.connect(self.__music_control)
        self.music_progress.sliderMoved.connect(self.__music_control)
        self._player.signal_music_unpause.connect(self.slot_music_unpause)
        self._player.signal_music_pause.connect(self.slot_music_pause)

        self.__paint_default_pic()

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.__init_local_list_widget()
        self.__init_setting()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.input_search.setPlaceholderText(_translate("MainWindow", "搜索歌曲"))
        self.volume_label.setText(_translate("MainWindow", "音量"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "本地"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "网络"))
        self.song_label.setText(_translate("MainWindow", "歌名"))
        self.singer_label.setText(_translate("MainWindow", "歌手"))
        self.curr_music_time.setText(_translate("MainWindow", "00:00"))
        self.full_music_time.setText(_translate("MainWindow", "00:00"))
        self.mc_prev.setText(_translate("MainWindow", "上一曲"))
        # self.mc_play_pause.setText(_translate("MainWindow", "播放"))
        self.mc_next.setText(_translate("MainWindow", "下一曲"))
        self.mc_play_pause.setStyleSheet("background-image: url(./res/play.png);")

    # 搜索
    def search(self):
        current_index = self.tabWidget.currentIndex()
        if current_index == 0:
            # TODO 本地搜索
            pass
        elif current_index == 1:
            self.__do_net_search()

    # 搜索网络资源
    def __do_net_search(self):
        self.net_list_widget.clear()
        title = self.input_search.text().title()
        # "我喜欢上你内心时的活动"
        sr = ReqUtils.search_music(title)
        for i, v in enumerate(sr, 1):
            Ui_MainWindow.__gen_list_item(self.net_list_widget, i, Converter.itooi_music(v))

    # 网络歌曲双击
    def net_list_widget_double_click(self, index_):
        self.__show_loading_music()
        self._player.stop()
        item = self.net_list_widget.item(index_.row())
        music = item.zak_music
        music.signal_load_over.connect(self.__music_download_over)
        self.music_progress.setEnabled(False)
        self.music_progress.setValue(0)
        self.curr_music_time.setText(TimeUtils.second2minute(0))
        self.full_music_time.setText(TimeUtils.second2minute(music.get_length()))
        self.song_label.setText(music.get_name())
        self.singer_label.setText(music.get_singer().replace("-", "/"))
        self._player.play(music)

    # 本地歌曲双击
    def local_list_widget_double_click(self, index_):
        self._player.stop()
        item = self.local_list_widget.item(index_.row())
        music = item.zak_music
        self.full_music_time.setText(TimeUtils.second2minute(music.get_length()))
        self.song_label.setText(music.get_name())
        self.singer_label.setText(music.get_singer().replace("-", "/"))
        self._player.play(music)
        pass

    # 音乐开始播放了响应方法
    def slot_music_start_play(self, music):
        self.__show_music(music)
        self.music_progress.setEnabled(True)
        # 刷新本地列表
        count = self.local_list_widget.count()
        for i in range(count):
            item = self.local_list_widget.item(i)
            if music == item.zak_music:
                return
        index = self._player.get_music_list().index(music)
        Ui_MainWindow.__gen_list_item(self.local_list_widget, index, music)

    def refresh_volume(self):
        value = self.volume_slider.value()
        self._player.set_volume(value)

    # 刷新进度条
    def __refresh_music_progress(self):
        if not self._player.is_play():
            return
        pos = self._player.get_pos()
        self.curr_music_time.setText(TimeUtils.second2minute(pos / 1000))
        self.music_progress.setValue(pos)

    # 绘制默认图片
    def __paint_default_pic(self):
        q_pixmap = QtGui.QPixmap("./res/default.jpg").scaled(self.pic_label.size(), QtCore.Qt.KeepAspectRatio)
        self.pic_label.setPixmap(q_pixmap)

    def __show_loading_music(self):
        movie = QMovie("./res/loding.gif")
        movie.setScaledSize(QtCore.QSize(50, 50))
        self.pic_label.setMovie(movie)
        movie.start()

    def __music_download_over(self, music):
        MusicDao.save(music)
        pass

    def __init_local_list_widget(self):
        all_ = MusicDao.get_all()
        for i, v in enumerate(all_, 1):
            Ui_MainWindow.__gen_list_item(self.local_list_widget, i, v)
        self._player.add_music_list(all_)

    def __init_setting(self):
        volume = SettingDao.get_volume()
        self._player.set_volume(volume)
        self.volume_slider.setValue(volume)
        last_id = SettingDao.get_last_music()
        pos = SettingDao.get_last_pos()
        by_id = MusicDao.get_by_music_id(last_id)
        if by_id is None:
            by_id = MusicDao.get_by_id(1)
            pos = 0
        if by_id is None:
            return
        self._player.load(by_id)
        self._player.set_pos(pos)
        self.__show_music(by_id)
        self.music_progress.setValue(pos)
        self.curr_music_time.setText(TimeUtils.second2minute(pos / 1000))

    def __show_music(self, music: Music):
        pic = music.get_pic()
        q_pixmap = QtGui.QPixmap(pic)
        q_pixmap = q_pixmap.scaled(self.pic_label.size(), QtCore.Qt.KeepAspectRatio)
        self.pic_label.setPixmap(q_pixmap)
        self.full_music_time.setText(TimeUtils.second2minute(music.get_length()))
        self.song_label.setText(music.get_name())
        self.singer_label.setText(music.get_singer().replace("-", "/"))
        self.music_progress.setMaximum(music.get_length() * 1000)

    # 快进，快退
    def __music_control(self):
        value = self.music_progress.value()
        self._player.set_pos(value)
        self.curr_music_time.setText(TimeUtils.second2minute(value / 1000))
        pass

    def slot_music_pause(self):
        self.mc_play_pause.setText("继续")

    def slot_music_unpause(self):
        self.mc_play_pause.setText("暂停")

    @staticmethod
    def __gen_list_item(list_widget: QtWidgets.QListWidget, index: int, music: Music):
        widget = QtWidgets.QWidget()
        mainArea = QtWidgets.QWidget()

        # 显示区域的布局
        verLayout = QtWidgets.QVBoxLayout()
        horLayout = QtWidgets.QHBoxLayout()

        # 主要控件
        id_label = QtWidgets.QLabel(widget)
        song_name_label = QtWidgets.QLabel(mainArea)
        singer_label = QtWidgets.QLabel(mainArea)

        # 设置不同控件的样式
        id_label.setFixedSize(30, 30)
        # id_label.setStyleSheet("background:red;border-radius:15px;color:black")
        id_label.setText(str(index))
        id_label.setAlignment(QtCore.Qt.AlignCenter)

        tempFont = QtGui.QFont("宋体", 12, 0)
        song_name_label.setObjectName("song_name_label")
        song_name_label.setText(music.get_name())
        song_name_label.setFont(tempFont)
        song_name_label.setFixedHeight(16)
        singer_label.setFixedSize(150, 16)
        singer_label.setObjectName("singer_label")
        singer_label.setText(music.get_singer())
        singer_label.setStyleSheet("color:gray;")

        verLayout.setContentsMargins(0, 0, 0, 0)
        verLayout.setSpacing(5)
        verLayout.addWidget(song_name_label)
        verLayout.addWidget(singer_label)
        mainArea.setLayout(verLayout)
        mainArea.setStyleSheet("border-bottom: 1px solid #e8e6dd;")

        horLayout.setContentsMargins(0, 0, 0, 0)
        horLayout.setSpacing(10)
        horLayout.addWidget(id_label)
        horLayout.addWidget(mainArea)
        widget.setLayout(horLayout)

        item = QtWidgets.QListWidgetItem()
        size = item.sizeHint()
        item.setSizeHint(QtCore.QSize(size.width(), 56))
        # list_widget.addItem(item)
        list_widget.insertItem(index, item)
        widget.setSizeIncrement(size.width(), 56)
        # widget.zak_music = core
        item.zak_music = music
        list_widget.setItemWidget(item, widget)

