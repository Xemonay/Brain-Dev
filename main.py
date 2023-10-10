import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from changeprofile import ChangeProfileForm
from questionmark import Creator
from list_of_games import ListOfGames
from random import choice as ch
from quick_math_ import QuickMath

if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)


class BrainDevMain(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Design//main0.ui', self)
        self.list_of_games_bt.clicked.connect(self.list_of_games_window)
        self.training_bt.clicked.connect(self.training)
        self.shop_bt.clicked.connect(self.test)
        self.settings_bt.clicked.connect(self.test)
        self.edit_profile_bt.clicked.connect(self.change_profile_form)
        self.what_is_that.clicked.connect(self.mystery_bt)

    def test(self):
        print("I clicked ->) ", self.sender().text())

    def change_profile_form(self):
        self.change_form = ChangeProfileForm(self)
        self.change_form.show()

    def list_of_games_window(self):
        self.list_of_games = ListOfGames(self)
        self.list_of_games.show()

    def training(self):
        eval(ch(["self.quick_math()", "self.math()", "self.attention()", "self.reaction()", "self.spatial_mem()",
                 "self.unscramble()"]))

    def quick_math(self):
        self.quickmath = QuickMath(self)
        self.quickmath.show()

    def math(self):
        print("1")

    def attention(self):
        print("1")

    def reaction(self):
        print("1")

    def spatial_mem(self):
        print("1")

    def unscramble(self):
        print("1")

    def mystery_bt(self):
        self.questionmark = Creator()
        self.questionmark.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BrainDevMain()
    ex.show()
    sys.exit(app.exec_())
