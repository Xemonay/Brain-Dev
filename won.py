import sqlite3

from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import QDialog

from DesingPY.won_game1 import Ui_Form


class WonGame(QDialog, Ui_Form):
    def __init__(self, other, main):
        super().__init__()
        self.setupUi(self)
        self.avg_sec.setText(str(round(sum(other.lsta) / other.count, 2)))
        self.mistake_l.setText(str(other.lstam))
        self.name_label.setText(main.username.text())
        self.okay_bt.clicked.connect(self.yeah)
        self.other = other
        self.main = main
        self.player = QMediaPlayer(self)
        self.player.setMedia(
            QMediaContent(QUrl.fromLocalFile(r"Sounds\WON!.wav")))
        self.player.setVolume(main.player.volume())
        if self.main.log:
            cor = sqlite3.connect("DataBases//accounts.sqlite")
            c = cor.cursor()
        match self.other.name:
            case "QM":
                if "9E9E9E" in self.main.status.styleSheet():
                    self.main.money += 1
                if self.main.log:
                    name = self.main.username.text()
                    a = c.execute("""SELECT quickmath FROM item
                                    WHERE name = ?""", (name,)).fetchone()[0]
                    if a == "0":
                        c.execute("""UPDATE item
                                    SET quickmath = '1'
                                    WHERE name = ?""", (name,))
                        c.execute("""UPDATE item
                                            SET money = money + 1
                                            WHERE name = ?""", (name,))
                    sec = float(c.execute("""SELECT avgsec FROM quickmath
                                        WHERE name = ?""", (name,)).fetchone()[0])
                    c.execute("""UPDATE quickmath
                                SET won = won + 1, played = played + 1, avgsec = ?, mistakes = mistakes + ?
                                WHERE name = ?""", (
                        str(round(sum(other.lsta) / other.count, 2)) if sec == 0.0 else str(
                            (round(sum(other.lsta) / other.count,
                                   2) + sec) / 2), other.lstam, name))
                self.main.status.setStyleSheet(self.main.qmstyle)
                asd = 0
            case "at":
                if "9E9E9E" in self.main.status_6.styleSheet():
                    self.main.money += 1
                if self.main.log:
                    name = self.main.username.text()
                    a = c.execute("""SELECT attention FROM item
                                    WHERE name = ?""", (name,)).fetchone()[0]
                    if a == "0":
                        c.execute("""UPDATE item
                                    SET attention = '1'
                                    WHERE name = ?""", (name,))
                        c.execute("""UPDATE item
                                            SET money = money + 1
                                            WHERE name = ?""", (name,))
                    sec = float(c.execute("""SELECT avgsec FROM attention
                                                            WHERE name = ?""", (name,)).fetchone()[0])
                    c.execute("""UPDATE attention
                                            SET won = won + 1, played = played + 1, avgsec = ?, mistakes = mistakes + ?
                                            WHERE name = ?""", (
                        str(round(sum(other.lsta) / other.count, 2)) if sec == 0.0 else str(
                            (round(sum(other.lsta) / other.count,
                                   2) + sec) / 2), other.lstam, name))
                self.main.status_6.setStyleSheet(self.main.atstyle)
                asd = 2
            case "go":
                if "9E9E9E" in self.main.status_2.styleSheet():
                    self.main.money += 1
                if self.main.log:
                    name = self.main.username.text()
                    a = c.execute("""SELECT goword FROM item
                                    WHERE name = ?""", (name,)).fetchone()[0]
                    if a == "0":
                        c.execute("""UPDATE item
                                    SET goword = '1'
                                    WHERE name = ?""", (name,))
                        c.execute("""UPDATE item
                                            SET money = money + 1
                                            WHERE name = ?""", (name,))
                    sec = float(c.execute("""SELECT avgsec FROM goword
                                                            WHERE name = ?""", (name,)).fetchone()[0])
                    c.execute("""UPDATE goword
                                            SET won = won + 1, played = played + 1, avgsec = ?, mistakes = mistakes + ?
                                            WHERE name = ?""", (
                        str(round(sum(other.lsta) / other.count, 2)) if sec == 0.0 else str(
                            (round(sum(other.lsta) / other.count,
                                   2) + sec) / 2), other.lstam, name))
                self.main.status_2.setStyleSheet(self.main.gostyle)
                asd = 1
            case "ra":
                if "9E9E9E" in self.main.status_5.styleSheet():
                    self.main.money += 1
                if self.main.log:
                    name = self.main.username.text()
                    a = c.execute("""SELECT reaction FROM item
                                    WHERE name = ?""", (name,)).fetchone()[0]
                    if a == "0":
                        c.execute("""UPDATE item
                                    SET reaction = '1'
                                    WHERE name = ?""", (name,))
                        c.execute("""UPDATE item
                                            SET money = money + 1
                                            WHERE name = ?""", (name,))
                    sec = float(c.execute("""SELECT avgsec FROM reaction
                                                            WHERE name = ?""", (name,)).fetchone()[0])
                    c.execute("""UPDATE reaction
                                            SET won = won + 1, played = played + 1, avgsec = ?, mistakes = mistakes + ?
                                            WHERE name = ?""", (
                        str(round(sum(other.lsta) / other.count, 2)) if sec == 0.0 else str(
                            (round(sum(other.lsta) / other.count,
                                   2) + sec) / 2), other.lstam, name))
                self.main.status_5.setStyleSheet(self.main.rastyle)
                asd = 3
            case "ua":
                if "9E9E9E" in self.main.status_7.styleSheet():
                    self.main.money += 1
                if self.main.log:
                    name = self.main.username.text()
                    a = c.execute("""SELECT unscramble FROM item
                                    WHERE name = ?""", (name,)).fetchone()[0]
                    if a == "0":
                        c.execute("""UPDATE item
                                    SET unscramble = '1'
                                    WHERE name = ?""", (name,))
                        c.execute("""UPDATE item
                                            SET money = money + 1
                                            WHERE name = ?""", (name,))
                    sec = float(c.execute("""SELECT avgsec FROM unscramble
                                                            WHERE name = ?""", (name,)).fetchone()[0])
                    c.execute("""UPDATE unscramble
                                            SET won = won + 1, played = played + 1, avgsec = ?, mistakes = mistakes + ?
                                            WHERE name = ?""", (
                        str(round(sum(other.lsta) / other.count, 2)) if sec == 0.0 else str(
                            (round(sum(other.lsta) / other.count,
                                   2) + sec) / 2), other.lstam, name))
                self.main.status_7.setStyleSheet(self.main.uastyle)
                asd = 4
            case "sa":
                if "9E9E9E" in self.main.status_8.styleSheet():
                    self.main.money += 1
                if self.main.log:
                    name = self.main.username.text()
                    a = c.execute("""SELECT spatialmem FROM item
                                    WHERE name = ?""", (name,)).fetchone()[0]
                    if a == "0":
                        c.execute("""UPDATE item
                                    SET spatialmem = '1'
                                    WHERE name = ?""", (name,))
                        c.execute("""UPDATE item
                                            SET money = money + 1
                                            WHERE name = ?""", (name,))
                    sec = float(c.execute("""SELECT avgsec FROM spatialmem
                                                            WHERE name = ?""", (name,)).fetchone()[0])
                    c.execute("""UPDATE spatialmem
                                            SET won = won + 1, played = played + 1, avgsec = ?, mistakes = mistakes + ?
                                            WHERE name = ?""", (
                        str(round(sum(other.lsta) / other.count, 2)) if sec == 0.0 else str(
                            (round(sum(other.lsta) / other.count,
                                   2) + sec) / 2), other.lstam, name))
                self.main.status_8.setStyleSheet(self.main.sastyle)
                asd = 5
        if self.main.lst_avgsec[asd] == 0:
            self.main.lst_avgsec[asd] = round(sum(other.lsta) / other.count, 2)
        else:
            self.main.lst_avgsec[asd] = round(
                (float(self.main.lst_avgsec[asd]) + round(sum(other.lsta) / other.count, 2)) / 2, 2)
        self.main.lst_mist[asd] += self.other.lstam
        self.main.lst_won[asd] += 1
        if self.main.log:
            cor.commit()
            cor.close()
        self.player.play()
        self.other.close()

    def yeah(self):
        self.player.stop()
        self.main.player.play()
        self.close()

    def closeEvent(self, event):
        self.player.stop()
        self.main.player.play()
