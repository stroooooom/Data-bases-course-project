# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_app2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        MainWindow.setMinimumSize(QtCore.QSize(500, 300))
        MainWindow.setMaximumSize(QtCore.QSize(500, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lword = QtWidgets.QLabel(self.centralwidget)
        self.lword.setGeometry(QtCore.QRect(10, 20, 111, 51))
        self.lword.setTextFormat(QtCore.Qt.PlainText)
        self.lword.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lword.setWordWrap(True)
        self.lword.setObjectName("lword")
        self.word = QtWidgets.QLineEdit(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(140, 30, 291, 21))
        self.word.setReadOnly(False)
        self.word.setObjectName("word")
        self.matchButton = QtWidgets.QPushButton(self.centralwidget)
        self.matchButton.setGeometry(QtCore.QRect(110, 60, 281, 41))
        self.matchButton.setMinimumSize(QtCore.QSize(281, 41))
        self.matchButton.setMaximumSize(QtCore.QSize(281, 41))
        self.matchButton.setObjectName("matchButton")
        self.soundList = QtWidgets.QListWidget(self.centralwidget)
        self.soundList.setGeometry(QtCore.QRect(30, 170, 441, 101))
        self.soundList.setMinimumSize(QtCore.QSize(248, 101))
        self.soundList.setMaximumSize(QtCore.QSize(16777215, 101))
        self.soundList.setSelectionRectVisible(False)
        self.soundList.setObjectName("soundList")
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(210, 120, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy)
        self.playButton.setMinimumSize(QtCore.QSize(41, 41))
        self.playButton.setMaximumSize(QtCore.QSize(41, 41))
        self.playButton.setBaseSize(QtCore.QSize(41, 41))
        self.playButton.setIconSize(QtCore.QSize(41, 41))
        self.playButton.setAutoDefault(False)
        self.playButton.setFlat(False)
        self.playButton.setObjectName("playButton")
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(260, 120, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy)
        self.stopButton.setMinimumSize(QtCore.QSize(41, 41))
        self.stopButton.setMaximumSize(QtCore.QSize(41, 41))
        self.stopButton.setBaseSize(QtCore.QSize(41, 41))
        self.stopButton.setIconSize(QtCore.QSize(41, 41))
        self.stopButton.setAutoDefault(False)
        self.stopButton.setFlat(False)
        self.stopButton.setObjectName("stopButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lword.setText(_translate("MainWindow", "Введите слово (по фонемам)"))
        self.matchButton.setText(_translate("MainWindow", "Подобрать"))
        self.playButton.setText(_translate("MainWindow", "▶"))
        self.stopButton.setText(_translate("MainWindow", "◾"))

