# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/raw_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 283)
        Dialog.setMinimumSize(QtCore.QSize(550, 0))
        Dialog.setMaximumSize(QtCore.QSize(1000, 5000))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.packetInfo = QtWidgets.QLabel(Dialog)
        self.packetInfo.setText("")
        self.packetInfo.setObjectName("packetInfo")
        self.verticalLayout.addWidget(self.packetInfo)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        self.textEdit.setFont(font)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.msg = QtWidgets.QLabel(Dialog)
        self.msg.setMaximumSize(QtCore.QSize(500, 250))
        self.msg.setText("")
        self.msg.setObjectName("msg")
        self.horizontalLayout.addWidget(self.msg)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.Dialog = Dialog

    def setText(self, text):
        self.textEdit.setText(text)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Data browser"))
