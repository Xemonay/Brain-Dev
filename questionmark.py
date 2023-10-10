from PyQt5 import uic
from PyQt5.QtWidgets import QDialog


class Creator(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Design//creator.ui', self)
