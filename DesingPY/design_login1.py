# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login1.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(328, 372)
        Form.setMinimumSize(QtCore.QSize(328, 372))
        Form.setMaximumSize(QtCore.QSize(328, 372))
        self.pass_e = QtWidgets.QLineEdit(Form)
        self.pass_e.setGeometry(QtCore.QRect(40, 160, 231, 31))
        self.pass_e.setText("")
        self.pass_e.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_e.setObjectName("pass_e")
        self.okay = QtWidgets.QPushButton(Form)
        self.okay.setGeometry(QtCore.QRect(100, 250, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(16)
        self.okay.setFont(font)
        self.okay.setStyleSheet("background-color:#FFD600;\n"
"color:white;\n"
"border-style: outset;\n"
"border-radius:10px;")
        self.okay.setObjectName("okay")
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(40, 40, 261, 31))
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.view = QtWidgets.QPushButton(Form)
        self.view.setGeometry(QtCore.QRect(0, 160, 31, 31))
        self.view.setStyleSheet("color: transparent;\n"
"background-color: transparent;\n"
"")
        self.view.setObjectName("view")
        self.bt_ture = QtWidgets.QLabel(Form)
        self.bt_ture.setGeometry(QtCore.QRect(0, 160, 31, 31))
        self.bt_ture.setObjectName("bt_ture")
        self.name_lal = QtWidgets.QLineEdit(Form)
        self.name_lal.setGeometry(QtCore.QRect(40, 80, 111, 31))
        self.name_lal.setText("")
        self.name_lal.setObjectName("name_lal")
        self.bt_ture.raise_()
        self.pass_e.raise_()
        self.okay.raise_()
        self.label_1.raise_()
        self.view.raise_()
        self.name_lal.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pass_e.setPlaceholderText(_translate("Form", "Pass"))
        self.okay.setText(_translate("Form", "Okay"))
        self.view.setText(_translate("Form", "PushButton"))
        self.bt_ture.setText(_translate("Form", "TextLabel"))
        self.name_lal.setPlaceholderText(_translate("Form", "Name"))