import sys
from PyQt5.QtCore import Qt
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from changeprofile import ChangeProfileForm

if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)


class BrainDevMain(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Design//main0.ui', self)
        self.list_of_games_bt.clicked.connect(self.test)
        self.training_bt.clicked.connect(self.test)
        self.shop_bt.clicked.connect(self.test)
        self.settings_bt.clicked.connect(self.test)
        self.edit_profile_bt.clicked.connect(self.change_profile_form)

    def test(self):
        print("I clicked ->) ", self.sender().text())

    def change_avatar(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        img = QImage(185, 205, QImage.Format_ARGB32)
        img.load(fname)
        self.avatar.setPixmap(QPixmap(img))

    def change_profile_form(self):
        self.change_form = ChangeProfileForm()
        self.change_form.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BrainDevMain()
    ex.show()
    sys.exit(app.exec_())
