import sqlite3

from PyQt5.QtWidgets import QDialog

from DesingPY.design_stat import Ui_Form


class Sta(QDialog, Ui_Form):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        name = main.sender().text()
        self.status.setText(name)
        self.status.setStyleSheet(main.sender().styleSheet())
        self.main = main
        if main.log:
            self.con = sqlite3.connect("DataBases//accounts.sqlite")
            self.c = self.con.cursor()
            match name:
                case "Quick Math":
                    a = self.c.execute("""SELECT * FROM quickmath
                                            WHERE name = ?""", (main.username.text(),)).fetchall()[0]
                case "GOWORD":
                    a = self.c.execute("""SELECT * FROM goword
                                            WHERE name = ?""", (main.username.text(),)).fetchall()[0]
                case "Attention":
                    a = self.c.execute("""SELECT * FROM attention
                                            WHERE name = ?""", (main.username.text(),)).fetchall()[0]
                case "Reaction":
                    a = self.c.execute("""SELECT * FROM reaction
                                            WHERE name = ?""", (main.username.text(),)).fetchall()[0]
                case "SpatialMem":
                    a = self.c.execute("""SELECT * FROM spatialmem
                                            WHERE name = ?""", (main.username.text(),)).fetchall()[0]
                case "Unscramble":
                    a = self.c.execute("""SELECT * FROM unscramble
                                                WHERE name = ?""", (main.username.text(),)).fetchall()[0]
            self.label_6.setText(str(a[3]))
            self.label_7.setText(str(a[4]))
            self.label_8.setText(a[2])
            self.label_9.setText(str(a[5]))
            self.label_10.setText(str(a[1]))
        else:
            match name:
                case "Quick Math":
                    asd = 0
                case "GOWORD":
                    asd = 1
                case "Attention":
                    asd = 2
                case "Reaction":
                    asd = 3
                case "SpatialMem":
                    asd = 4
                case "Unscramble":
                    asd = 5
            self.label_6.setText(str(main.lst_won[asd]))
            self.label_7.setText(str(main.lst_lost[asd]))
            self.label_8.setText(str(main.lst_avgsec[asd]))
            self.label_9.setText(str(main.lst_mist[asd]))
            self.label_10.setText(str(main.lst_won[asd] + main.lst_lost[asd]))

    def closeEvent(self, a0):
        if self.main.log:
            self.con.commit()
            self.con.close()
