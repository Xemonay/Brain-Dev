from PyQt5.QtWidgets import QDialog

from DesingPY.creatordesign import Ui_Form


class Creator(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
