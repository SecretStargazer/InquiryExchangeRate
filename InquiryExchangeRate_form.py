# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InquiryExchangeRate_form.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.currencyName2 = QtWidgets.QComboBox(self.centralwidget)
        self.currencyName2.setGeometry(QtCore.QRect(400, 40, 150, 22))
        self.currencyName2.setObjectName("currencyName2")
        self.currencyName1 = QtWidgets.QComboBox(self.centralwidget)
        self.currencyName1.setGeometry(QtCore.QRect(150, 40, 150, 22))
        self.currencyName1.setObjectName("currencyName1")
        self.currencyAmount1 = QtWidgets.QLineEdit(self.centralwidget)
        self.currencyAmount1.setGeometry(QtCore.QRect(30, 40, 80, 20))
        self.currencyAmount1.setObjectName("currencyAmount1")
        self.exchangeButton = QtWidgets.QPushButton(self.centralwidget)
        self.exchangeButton.setGeometry(QtCore.QRect(325, 40, 50, 23))
        self.exchangeButton.setObjectName("exchangeButton")
        self.supportTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.supportTextLabel.setGeometry(QtCore.QRect(30, 120, 400, 12))
        self.supportTextLabel.setObjectName("supportTextLabel")
        self.resultTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultTextLabel.setGeometry(QtCore.QRect(30, 80, 400, 12))
        self.resultTextLabel.setObjectName("resultTextLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exchangeButton.setText(_translate("MainWindow", "转换"))
        self.supportTextLabel.setText(_translate("MainWindow", "数据仅供参考，交易时以银行柜台成交价为准 更新时间:"))
        self.resultTextLabel.setText(_translate("MainWindow", "结果"))


