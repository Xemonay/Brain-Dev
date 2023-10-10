from PyQt5 import uic
from PyQt5.QtWidgets import QDialog


class OhNo(QDialog):
    def __init__(self, other, main):
        super().__init__()
        uic.loadUi('Design//oh_noo.ui', self)
        self.try_again_bt.clicked.connect(self.again)
        self.quit_bt.clicked.connect(self.yeah)
        self.other = other
        self.main = main

    def yeah(self):
        self.other.close()
        self.close()

    def again(self):
        self.other.close()
        self.main.quick_math()
        self.close()