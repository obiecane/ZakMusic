import imghdr
import json
import logging
import sys
import time

import pygame
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow
from mutagen.mp3 import MP3

import com.zak.ui.LYTMusic as lyt_music
from com.zak.utils.Converter import Converter
from com.zak.utils.MusicUtils import MusicUtils

log_file_name = time.strftime('%Y-%m-%d', time.localtime(time.time()))

# 新增 fh，修改 basicConfig
fh = logging.FileHandler(encoding='utf-8', mode='a', filename="./log/" + log_file_name + ".log")
# logging.basicConfig(handlers=[fh], format='[%(asctime)s %(levelname)s]<%(process)d> %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

logging.basicConfig(level=logging.DEBUG,
                    handlers=[fh],
                    format='%(asctime)s \tFile \"%(filename)s\"[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def test():
    m = MusicUtils()
    m.play("F:\CloudMusic\李宗盛\李宗盛 - 山丘 (Live).mp3")


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
    MainWindow = QMainWindow()
    ui = lyt_music.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    pass


def test4():
    imghdr.test()
    imgType = imghdr.what("./music/Chan/分分钟需要你（Cover：林子祥）.mp3")
    print(imgType)


if __name__ == "__main__":
    test3()
