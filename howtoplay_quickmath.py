from PyQt5.QtWidgets import QDialog
from quick_math_ import QuickMath
from howtoplay_quickmathdesign import Ui_Form


class HowToPlay(QDialog, Ui_Form):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setupUi(self)
        self.start_bt.clicked.connect(self.play)

    def play(self):
        self.quickmath = QuickMath(self.main, self)
        self.main.player.pause()
        self.quickmath.show()
