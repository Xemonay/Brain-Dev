from PyQt5.QtWidgets import QMainWindow
from list_of_gamesdesign import Ui_MainWindow

class ListOfGames(QMainWindow, Ui_MainWindow):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.main = main
        self.quick_math_bt.clicked.connect(self.quick_math)
        self.math_bt.clicked.connect(self.math)
        self.attention_bt.clicked.connect(self.attention)
        self.reaction_bt.clicked.connect(self.reaction)
        self.spatial_mem_bt.clicked.connect(self.spatial_mem)
        self.unscramble_bt.clicked.connect(self.unscramble)

    def quick_math(self):
        self.main.quick_math()
        self.close()

    def math(self):
        self.main.math()
        self.close()

    def attention(self):
        self.main.attention()
        self.close()

    def reaction(self):
        self.main.reaction()
        self.close()

    def spatial_mem(self):
        self.main.spatial_mem()
        self.close()

    def unscramble(self):
        self.main.unscramble()
        self.close()
