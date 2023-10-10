from PyQt5 import uic
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QFileDialog


class ChangeProfileForm(QDialog):
    def __init__(self, main):
        super().__init__()
        self.main = main
        uic.loadUi('Design//changeform.ui', self)
        self.change_avatar_bt.clicked.connect(self.change_avatar)
        self.okay_name_bt.clicked.connect(self.change_name)
        self.okay_age_bt.clicked.connect(self.change_age)

    def change_avatar(self):
        fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        img = QImage(185, 205, QImage.Format_ARGB32)
        img.load(fname)
        self.file_name_label.setText(fname)
        self.main.avatar.setPixmap(QPixmap(img))

    def change_name(self):
        self.main.username.setText(self.change_name_edt.text())

    def change_age(self):
        try:
            self.main.age.setText("Age = " + str(int(self.change_age_edt.text())))
            self.not_correct_age_label.setText("")
        except ValueError:
            self.not_correct_age_label.setText("Not correct age entered")