from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QLabel


class MyPicLabel(QLabel):
    clicked = pyqtSignal()

    def mouseReleaseEvent(self, e: QMouseEvent):
        self.clicked.emit()
