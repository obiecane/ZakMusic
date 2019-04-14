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

# QSlider::handle:horizontal { /*水平滑块的手柄*/
#         image: url(:/image/sliderHandle.png);
#  }
#
# QSlider::sub-page:horizontal { /*水平滑块手柄以前的部分*/
#         border-image: url(:/image/slider.png);/*边框图片*/
#  }

# QSlider::groove: horizontal
# {
#     border: 1px solid  # 4A708B;
#     background:  # C0C0C0;
#         height: 5
# px;
# border - radius: 1
# px;
# padding - left: -1
# px;
# padding - right: -1
# px;
# }
#
# QSlider::sub - page: horizontal
# {
#     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
# stop: 0  # B1B1B1, stop:1 #c4c4c4);
# background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,
# stop: 0  # 5DCCFF, stop: 1 #1874CD);
# border: 1
# px
# solid  # 4A708B;
# height: 10
# px;
# border - radius: 2
# px;
# }
#
# QSlider::add - page: horizontal
# {
#     background:  # 575757;
#         border: 0
# px
# solid  # 777;
# height: 10
# px;
# border - radius: 2
# px;
# }
#
# QSlider::handle: horizontal
# {
#     background: qradialgradient(spread: pad, cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5,
# stop: 0.6  # 45ADED, stop:0.778409 rgba(255, 255, 255, 255));
#
# width: 11
# px;
# margin - top: -3
# px;
# margin - bottom: -3
# px;
# border - radius: 5
# px;
# }
#
# QSlider::handle: horizontal:hover
# {
#     background: qradialgradient(spread: pad, cx: 0.5, cy: 0.5, radius: 0.5, fx: 0.5, fy: 0.5, stop: 0.6  # 2A8BDA,
# stop: 0.778409
# rgba(255, 255, 255, 255));
#
# width: 11
# px;
# margin - top: -3
# px;
# margin - bottom: -3
# px;
# border - radius: 5
# px;
# }
#
# QSlider::sub - page: horizontal:disabled
# {
#     background:  # 00009C;
#         border - color:  # 999;
# }
#
# QSlider::add - page: horizontal:disabled
# {
#     background:  # eee;
#         border - color:  # 999;
# }
#
# QSlider::handle: horizontal:disabled
# {
#     background:  # eee;
#         border: 1
# px
# solid  # aaa;
# border - radius: 4
# px;
# }
