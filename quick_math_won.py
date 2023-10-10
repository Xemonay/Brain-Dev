from PyQt5 import uic
from PyQt5.QtWidgets import QDialog


class WonGame(QDialog):
    def __init__(self, other, main):
        super().__init__()
        uic.loadUi('Design//won_game_quick_math.ui', self)
        self.avg_sec.setText(str(sum(other.lsta) / 10))
        self.name_label.setText(main.username.text())
        self.okay_bt.clicked.connect(self.yeah)
        self.other = other

    def yeah(self):
        self.other.close()
        self.close()
