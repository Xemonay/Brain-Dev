from PyQt5.QtWidgets import QDialog
from attention import Attention
from PyQt5 import uic


class HowToPlayA(QDialog):
    def __init__(self, main):
        super().__init__()
        uic.loadUi('Design//howtoplayattention.ui', self)
        self.main = main
        self.start_bt.clicked.connect(self.play)

    def play(self):
        self.attention = Attention(self.main, self)
        self.main.player.pause()
        self.attention.show()
