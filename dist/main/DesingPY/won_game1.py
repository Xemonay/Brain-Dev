# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'won_game.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 0, 271, 61))
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.name_label = QtWidgets.QLabel(Form)
        self.name_label.setGeometry(QtCore.QRect(60, 50, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.okay_bt = QtWidgets.QPushButton(Form)
        self.okay_bt.setGeometry(QtCore.QRect(60, 250, 75, 23))
        self.okay_bt.setObjectName("okay_bt")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(210, 30, 150, 221))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Pictures//gold-trophy-cup-11-h-ec5152g.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 140, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.avg_sec = QtWidgets.QLabel(Form)
        self.avg_sec.setGeometry(QtCore.QRect(140, 140, 47, 13))
        self.avg_sec.setObjectName("avg_sec")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 111, 16))
        self.label_2.setObjectName("label_2")
        self.mistake_l = QtWidgets.QLabel(Form)
        self.mistake_l.setGeometry(QtCore.QRect(140, 170, 47, 13))
        self.mistake_l.setObjectName("mistake_l")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Congradulations!"))
        self.name_label.setText(_translate("Form", "TextLabel"))
        self.okay_bt.setText(_translate("Form", "Okay"))
        self.label_4.setText(_translate("Form", "Your average time was:"))
        self.avg_sec.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "Mistakes were made:"))
        self.mistake_l.setText(_translate("Form", "TextLabel"))