from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QSlider


class MyQSlider(QSlider):
    hitSliderClicked = pyqtSignal()

    def mousePressEvent(self, ev):
        super().mousePressEvent(ev)
        pos = ev.pos().x() / self.width()

        self.setValue(pos * (self.maximum() - self.minimum()) + self.minimum())
        self.hitSliderClicked.emit()
