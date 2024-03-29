# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LYTMusic.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QMovie

from com.zak.core.Music import Music
from com.zak.core.Player import Player
from com.zak.core.Searcher import Searcher
from com.zak.dao.MusicDao import MusicDao
from com.zak.dao.SettingDao import SettingDao
from com.zak.ui.MyPicLabel import MyPicLabel
from com.zak.ui.MyQSlider import MyQSlider
from com.zak.utils.Converter import Converter
from com.zak.utils.LrcUtils import LrcUtils
from com.zak.utils.TimeUtils import TimeUtils


class Ui_MainWindow(object):

    # 滑块组件的颜色， 滑块的图片
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

    # 去掉listWidget的边框
    __QListWidget_Qss = "QListWidget{border:0px solid black;}"

    __QListWidget_Item_Qss = "QListWidgetItem{border-bottom: 1px solid gray;}"

    # 下一首按钮的样式
    __MC_NEXT_QSS = "QPushButton{border-image: url(./res/mc/next.png);} \
            QPushButton:hover{border-image: url(./res/mc/next-1.png);} \
            QPushButton:pressed{border-image: url(./res/mc/next-1.png);}"

    __MC_PLAY_QSS = "QPushButton{border-image: url(./res/mc/play.png);} \
                QPushButton:hover{border-image: url(./res/mc/play-1.png);} \
                QPushButton:pressed{border-image: url(./res/mc/play-1.png);}"

    __MC_PAUSE_QSS = "QPushButton{border-image: url(./res/mc/pause.png);} \
                    QPushButton:hover{border-image: url(./res/mc/pause-1.png);} \
                    QPushButton:pressed{border-image: url(./res/mc/pause-1.png);}"

    __MC_PREV_QSS = "QPushButton{border-image: url(./res/mc/prev.png);} \
                QPushButton:hover{border-image: url(./res/mc/prev-1.png);} \
                QPushButton:pressed{border-image: url(./res/mc/prev-1.png);}"

    def __init__(self):
        super().__init__()
        self._player = Player()
        self._searcher = Searcher()
        self._music_timer = QTimer()
        self._music_timer.timeout.connect(self.__refresh_music_progress)  # 计时结束调用operate()方法
        self._music_timer.start(1000)  # 设置计时间隔并启动


    def setupUi(self, MainWindow):
        MainWindow.ui = self
        MainWindow.player = self._player
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(380, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.input_search = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.input_search.setFont(font)
        self.input_search.setInputMask("")
        self.input_search.setText("")
        self.input_search.setObjectName("input_search")
        self.verticalLayout_2.addWidget(self.input_search)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.volume_label = QtWidgets.QLabel(self.centralwidget)
        self.volume_label.setMinimumSize(QtCore.QSize(5, 5))
        q_pixmap = QtGui.QPixmap("./res/voice/voice3.png").scaled(QtCore.QSize(20, 20), QtCore.Qt.KeepAspectRatio)
        self.volume_label.setPixmap(q_pixmap)
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
        self.tabWidget.setMinimumWidth(362)
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
        self.stackedWidget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.local_list_widget = QtWidgets.QListWidget(self.page_3)
        self.local_list_widget.setObjectName("local_list_widget")
        self.verticalLayout_6.addWidget(self.local_list_widget)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(20, 115, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.page_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(300, 300))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 114, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem3)
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
        self.net_list_widget.setObjectName("net_list_widget")
        self.verticalLayout_7.addWidget(self.net_list_widget)
        self.stackedWidget_3.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        spacerItem4 = QtWidgets.QSpacerItem(20, 115, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(self.page_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(300, 300))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 114, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem7)
        self.stackedWidget_3.addWidget(self.page_6)
        self.verticalLayout_4.addWidget(self.stackedWidget_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.stackedWidget.addWidget(self.page)

        self.lrc_page = QtWidgets.QWidget()
        self.lrc_page.setObjectName("lrc_page")
        self.lrc_verticalLayout = QtWidgets.QVBoxLayout(self.lrc_page)
        self.lrc_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lrc_verticalLayout.setObjectName("lrc_verticalLayout")
        self.lrc_browser = QtWidgets.QTextBrowser(self.lrc_page)
        self.lrc_browser.setObjectName("textEdit")
        self.lrc_verticalLayout.addWidget(self.lrc_browser)
        self.lrc_browser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lrc_browser.setFont(font)

        self.lrc_browser.setText("歌词显示。。。")
        self.lrc_browser.setAlignment(QtCore.Qt.AlignCenter)

        self.stackedWidget.addWidget(self.lrc_page)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pic_label = MyPicLabel(self.centralwidget)
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
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
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
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.mc_prev = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mc_prev.sizePolicy().hasHeightForWidth())
        self.mc_prev.setSizePolicy(sizePolicy)
        self.mc_prev.setMinimumSize(QtCore.QSize(42, 42))
        self.mc_prev.setText("")
        self.mc_prev.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mc_prev.setObjectName("mc_prev")
        self.horizontalLayout_2.addWidget(self.mc_prev)
        spacerItem10 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.mc_play_pause = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mc_play_pause.sizePolicy().hasHeightForWidth())
        self.mc_play_pause.setSizePolicy(sizePolicy)
        self.mc_play_pause.setMinimumSize(QtCore.QSize(50, 50))
        self.mc_play_pause.setAutoFillBackground(False)
        self.mc_play_pause.setText("")
        self.mc_play_pause.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mc_play_pause.setObjectName("mc_play_pause")
        self.horizontalLayout_2.addWidget(self.mc_play_pause)
        spacerItem11 = QtWidgets.QSpacerItem(10, 5, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        self.mc_next = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mc_next.sizePolicy().hasHeightForWidth())
        self.mc_next.setSizePolicy(sizePolicy)
        self.mc_next.setMinimumSize(QtCore.QSize(42, 42))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        self.mc_next.setFont(font)
        self.mc_next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mc_next.setText("")
        self.mc_next.setObjectName("mc_next")
        self.horizontalLayout_2.addWidget(self.mc_next)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(3, 4)
        self.horizontalLayout_2.setStretch(5, 3)
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
        self._searcher.signal_search_begin.connect(self.slot_net_search_begin)
        self._searcher.signal_search_success.connect(self.slot_net_search_success)
        self._searcher.signal_search_fail.connect(self.slot_net_search_fail)
        self.pic_label.clicked.connect(self.pic_clicked)
        self.__paint_default_pic()

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.__init_local_list_widget()
        self.__init_setting()

    def retranslateUi(self, MainWindow):
        self.__main_window = MainWindow
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "叼炸天播放器！？？Σ(っ °Д °;)っ"))
        MainWindow.setWindowIcon(QtGui.QIcon("./res/dog-logo.jpg"))
        self.input_search.setPlaceholderText(_translate("MainWindow", "搜索歌曲"))
        # self.volume_label.setText(_translate("MainWindow", "音量"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "本地"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "网络"))
        self.song_label.setText(_translate("MainWindow", "歌名"))
        self.singer_label.setText(_translate("MainWindow", "歌手"))
        self.curr_music_time.setText(_translate("MainWindow", "00:00"))
        self.full_music_time.setText(_translate("MainWindow", "00:00"))
        self.mc_next.setStyleSheet(Ui_MainWindow.__MC_NEXT_QSS)
        self.mc_prev.setStyleSheet(Ui_MainWindow.__MC_PREV_QSS)
        self.mc_play_pause.setStyleSheet(Ui_MainWindow.__MC_PLAY_QSS)
        self.local_list_widget.setStyleSheet(Ui_MainWindow.__QListWidget_Qss)
        self.net_list_widget.setStyleSheet(Ui_MainWindow.__QListWidget_Qss)
        movie = QMovie("./res/loding-2.gif")
        movie.setScaledSize(QtCore.QSize(300, 300))
        self.label.setMovie(movie)
        self.label_2.setMovie(movie)

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
        self.net_list_widget.scrollToTop()
        title = self.input_search.text().title()
        self._searcher.search_music(title)

    def slot_net_search_begin(self):
        self.label_2.movie().start()
        self.stackedWidget_3.setCurrentIndex(1)

    def slot_net_search_success(self, music_list: list):
        for i, v in enumerate(music_list):
            Ui_MainWindow.__gen_list_item(self.net_list_widget, i, Converter.itooi_music(v))
        self.stackedWidget_3.setCurrentIndex(0)
        self.label_2.movie().stop()

    def slot_net_search_fail(self):
        self.stackedWidget_3.setCurrentIndex(0)
        self.label_2.movie().stop()
        QtWidgets.QMessageBox.information(self.__main_window, 'zak music', '╮（╯＿╰）╭\n搜索失败', QtWidgets.QMessageBox.Yes,
                                          QtWidgets.QMessageBox.Yes)

    # 网络歌曲双击
    def net_list_widget_double_click(self, index_):
        self.__show_loading_music()
        self._player.stop()
        item = self.net_list_widget.item(index_.row())
        music = item.zak_music
        music.signal_load_over.connect(self.__music_download_over)
        music.signal_load_fail.connect(self.__music_download_fail)
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

    def pic_clicked(self):
        i = self.stackedWidget.currentIndex()
        i = 1 if i == 0 else 0
        self.stackedWidget.setCurrentIndex(i)
        pass

    # 音乐开始播放了响应方法
    def slot_music_start_play(self, music):
        self.__show_music(music)
        self.music_progress.setEnabled(True)
        self.mc_play_pause.setStyleSheet(Ui_MainWindow.__MC_PAUSE_QSS)
        lrc = LrcUtils.read_lrc(music.get_lrc())
        self.lrc_browser.setText(lrc)
        # 刷新本地列表
        count = self.local_list_widget.count()
        for i in range(count):
            item = self.local_list_widget.item(i)
            if music == item.zak_music:
                return
        index = self._player.get_music_list().index(music)
        Ui_MainWindow.__gen_list_item(self.local_list_widget, index, music)
        # 更新之后index之后的序号
        count = self.local_list_widget.count()
        for i in range(index + 1, count):
            item = self.local_list_widget.item(i)
            widget = self.local_list_widget.itemWidget(item)
            id_label = widget.findChild(QtWidgets.QLabel, "id_label")
            id_label.setText(str(i + 1))


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

    # 歌曲加载失败
    def __music_download_fail(self):
        self._player.play_next()
        pass

    def __init_local_list_widget(self):
        all_ = MusicDao.get_all()
        for i, v in enumerate(all_):
            Ui_MainWindow.__gen_list_item(self.local_list_widget, i, v)
        self._player.add_music_list(all_)

    # 初始化播放器相关设置(音量， 最后播放的歌曲id， 最后播放歌曲的位置)
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
        self.mc_play_pause.setStyleSheet(Ui_MainWindow.__MC_PLAY_QSS)

    def slot_music_unpause(self):
        self.mc_play_pause.setStyleSheet(Ui_MainWindow.__MC_PAUSE_QSS)

    # 通过歌曲创建列表项
    @staticmethod
    def __gen_list_item(list_widget: QtWidgets.QListWidget, index: int, music: Music):
        widget = QtWidgets.QWidget()
        mainArea = QtWidgets.QWidget()

        # 显示区域的布局
        verLayout = QtWidgets.QVBoxLayout()
        horLayout = QtWidgets.QHBoxLayout()

        # 主要控件
        id_label = QtWidgets.QLabel(widget)
        id_label.setObjectName("id_label")
        song_name_label = QtWidgets.QLabel(mainArea)
        singer_label = QtWidgets.QLabel(mainArea)

        # 设置不同控件的样式
        id_label.setFixedSize(30, 30)
        # id_label.setStyleSheet("background:red;border-radius:15px;color:black")
        id_label.setText(str(index + 1))
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
