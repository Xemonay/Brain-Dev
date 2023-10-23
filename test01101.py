import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush


class BrainDevMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)
        self.resize(500, 500)
        pixmap = QPixmap("Pictures//Circle_(transparent).png")
        pal = self.palette()
        pal.setBrush(QPalette.ColorGroup.Normal, QPalette.ColorRole.Window, QBrush(pixmap))
        self.setPalette(pal)
        self.setMask(pixmap.mask())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BrainDevMain()
    ex.show()
    sys.exit(app.exec_())
