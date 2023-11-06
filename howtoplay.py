from PyQt5.QtWidgets import QDialog
from Modules.attention import Attention
from Modules.quick_math_ import QuickMath
from Modules.reaction import Reaction
from Modules.spatialmem import SpatialMem
from Modules.unscramble import Unscramble
from Modules.goword import GOWORD


class Choice:
    def __init__(self, main, choice):
        designs = {"Attention": "Attention(self.main, self)",
                   "QuickMath": "QuickMath(self.main, self)",
                   "Reaction": "Reaction(self.main, self)",
                   "SpatialMem": "SpatialMem(self.main, self)",
                   "Unscramble": "Unscramble(self.main, self)",
                   "GOWORD": "GOWORD(self.main, self)"}
        match choice:
            case "Attention":
                from DesingPY.howtoplayattentiondesign import Ui_Form
            case "QuickMath":
                from DesingPY.howtoplay_quickmathdesign import Ui_Form
            case "Reaction":
                from DesingPY.howtoplayreactiondesign import Ui_Form
            case "SpatialMem":
                from DesingPY.howtoplayspatialmemdesign import Ui_Form
            case "Unscramble":
                from DesingPY.howtoplay_unscramble import Ui_Form
            case "GOWORD":
                from DesingPY.howtoplay_goworddesign import Ui_Form

        class HowToPlay(QDialog, Ui_Form):
            def __init__(self, main, gamemode):
                super().__init__()
                self.mode = gamemode
                self.setupUi(self)
                self.main = main
                self.start_bt.clicked.connect(self.play)

            def play(self):
                self.modeplay = eval(self.mode)
                self.main.player.pause()
                self.modeplay.show()

        self.a = HowToPlay(main, designs.get(choice))
        self.a.show()