# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(509, 372)
        Form.setMinimumSize(QtCore.QSize(509, 372))
        Form.setMaximumSize(QtCore.QSize(509, 372))
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.name_lal = QtWidgets.QLineEdit(Form)
        self.name_lal.setGeometry(QtCore.QRect(50, 90, 111, 31))
        self.name_lal.setObjectName("name_lal")
        self.pass_e = QtWidgets.QLineEdit(Form)
        self.pass_e.setGeometry(QtCore.QRect(50, 160, 231, 31))
        self.pass_e.setText("")
        self.pass_e.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_e.setObjectName("pass_e")
        self.label6 = QtWidgets.QLabel(Form)
        self.label6.setGeometry(QtCore.QRect(180, 100, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.label6.setFont(font)
        self.label6.setObjectName("label6")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(310, 170, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.okay = QtWidgets.QPushButton(Form)
        self.okay.setGeometry(QtCore.QRect(190, 250, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.okay.setFont(font)
        self.okay.setStyleSheet("background-color:#FFD600;\n"
"color:white;\n"
"border-style: outset;\n"
"border-radius:10px;")
        self.okay.setObjectName("okay")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 200, 261, 31))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(50, 120, 261, 31))
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 50, 261, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.view = QtWidgets.QPushButton(Form)
        self.view.setGeometry(QtCore.QRect(10, 160, 31, 31))
        self.view.setStyleSheet("background-color: transparent;\n"
"color: transparent;\n"
"")
        self.view.setObjectName("view")
        self.bt_ture = QtWidgets.QLabel(Form)
        self.bt_ture.setGeometry(QtCore.QRect(10, 160, 31, 31))
        self.bt_ture.setObjectName("bt_ture")
        self.bt_ture.raise_()
        self.name_lal.raise_()
        self.pass_e.raise_()
        self.label6.raise_()
        self.label_2.raise_()
        self.okay.raise_()
        self.label_6.raise_()
        self.label_1.raise_()
        self.label.raise_()
        self.view.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name_lal.setPlaceholderText(_translate("Form", "Name"))
        self.pass_e.setPlaceholderText(_translate("Form", "Pass"))
        self.label6.setText(_translate("Form", "Max 10, min 2"))
        self.label_2.setText(_translate("Form", "Min 6 Max 16"))
        self.okay.setText(_translate("Form", "Okay"))
        self.view.setText(_translate("Form", "PushButton"))
        self.bt_ture.setText(_translate("Form", "TextLabel"))
