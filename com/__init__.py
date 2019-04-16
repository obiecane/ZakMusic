import imghdr
import json
import logging
import sqlite3
import sys
import time

import pygame
import requests
from PyQt5.QtWidgets import QApplication
from mutagen.mp3 import MP3

import com.zak.ui.LYTMusic as lyt_music
from com.zak.dao.MusicDao import MusicDao
from com.zak.ui.MyQMainWindow import MyQMainWindow
from com.zak.utils.Converter import Converter
from com.zak.utils.DBUtils import DBUtils
from com.zak.utils.MusicUtils import MusicUtils
from com.zak.utils.QssUtils import QssUtils

log_file_name = time.strftime('%Y-%m-%d', time.localtime(time.time()))

# 新增 fh，修改 basicConfig
fh = logging.FileHandler(encoding='utf-8', mode='a', filename="./log/" + log_file_name + ".log")
# logging.basicConfig(handlers=[fh], format='[%(asctime)s %(levelname)s]<%(process)d> %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

logging.basicConfig(level=logging.DEBUG,
                    handlers=[fh],
                    format='%(asctime)s \tFile \"%(filename)s\"[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def test1():
    file = u"F:\CloudMusic\李宗盛\李宗盛 - 山丘 (Live).mp3"
    mp_ = MP3(file)

    url = "https://api.itooi.cn/music/netease/song?key=579621905&id=1356132066"
    get = requests.get(url)
    json_result = json.loads(get.content.decode())
    music = Converter.itooi_music(json_result)
    music.get_uri()
    time.sleep(15)
    pygame.mixer.music.pause()
    time.sleep(3)
    pygame.mixer.music.unpause()
    print("test 1 over")


def test3():
    app = QApplication(sys.argv)
    MainWindow = MyQMainWindow()
    ui = lyt_music.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    pass


def test4():
    imghdr.test()
    imgType = imghdr.what("./music/Chan/分分钟需要你（Cover：林子祥）.mp3")
    print(imgType)


def test_db():
    # 打开连接
    conn = sqlite3.connect("lyt_music.db")
    sql = ""
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
    except Exception as e:
        pass

    sql = "insert into login (id, name, password) values ('1', 'love', '520520')"
    cursor.execute(sql)
    sql = "insert into login (id, name, password) values ('2', 'hate', '000000')"
    cursor.execute(sql)

    sql = "select * from login"
    cursor.execute(sql)

    values = cursor.fetchall()
    for v in values:
        print(v[1])
    print(values)


def __create_database():
    sql = "create table login (id varchar(20) primary key, name varchar(30), password varchar(30))"


def test_pygame_event():
    pygame.mixer.music.load("./music/李宗盛/问.mp3")
    pygame.mixer.music.queue("./music/任然/空空如也 .mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(8)

    while True:
        busy = pygame.mixer.music.get_busy()
        endevent = pygame.mixer.music.get_endevent()
        if busy == 1 and endevent == 0:
            continue
        print(busy)
        print(endevent)
        print("-----------------------------")
        time.sleep(1)


if __name__ == "__main__":
    DBUtils.init_tables()
    test3()
    # test_db()
    # test_pygame_event()
