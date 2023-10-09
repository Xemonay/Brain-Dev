from PyQt5.QtWidgets import QDialog
from PyQt5 import uic


class ChangeProfileForm(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Design//changeform.ui', self)
