# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_app1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 719)
        MainWindow.setMinimumSize(QtCore.QSize(248, 3))
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.soundSubwindow = QtWidgets.QFrame(self.centralwidget)
        self.soundSubwindow.setGeometry(QtCore.QRect(0, 90, 781, 591))
        self.soundSubwindow.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.soundSubwindow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.soundSubwindow.setObjectName("soundSubwindow")
        self.zoomInButton = QtWidgets.QPushButton(self.soundSubwindow)
        self.zoomInButton.setEnabled(True)
        self.zoomInButton.setGeometry(QtCore.QRect(60, 10, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomInButton.sizePolicy().hasHeightForWidth())
        self.zoomInButton.setSizePolicy(sizePolicy)
        self.zoomInButton.setMinimumSize(QtCore.QSize(41, 41))
        self.zoomInButton.setMaximumSize(QtCore.QSize(41, 41))
        self.zoomInButton.setBaseSize(QtCore.QSize(41, 41))
        self.zoomInButton.setIconSize(QtCore.QSize(41, 41))
        self.zoomInButton.setObjectName("zoomInButton")
        self.stopButton = QtWidgets.QPushButton(self.soundSubwindow)
        self.stopButton.setGeometry(QtCore.QRect(400, 10, 41, 41))
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
        self.zoomOutButton = QtWidgets.QPushButton(self.soundSubwindow)
        self.zoomOutButton.setGeometry(QtCore.QRect(10, 10, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomOutButton.sizePolicy().hasHeightForWidth())
        self.zoomOutButton.setSizePolicy(sizePolicy)
        self.zoomOutButton.setMinimumSize(QtCore.QSize(41, 41))
        self.zoomOutButton.setMaximumSize(QtCore.QSize(41, 41))
        self.zoomOutButton.setBaseSize(QtCore.QSize(41, 41))
        self.zoomOutButton.setIconSize(QtCore.QSize(41, 41))
        self.zoomOutButton.setAutoDefault(False)
        self.zoomOutButton.setFlat(False)
        self.zoomOutButton.setObjectName("zoomOutButton")
        self.playButton = QtWidgets.QPushButton(self.soundSubwindow)
        self.playButton.setGeometry(QtCore.QRect(350, 10, 41, 41))
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
        self.audioScrollArea = QtWidgets.QScrollArea(self.soundSubwindow)
        self.audioScrollArea.setGeometry(QtCore.QRect(10, 60, 761, 150))
        self.audioScrollArea.setMinimumSize(QtCore.QSize(761, 150))
        self.audioScrollArea.setMaximumSize(QtCore.QSize(761, 150))
        self.audioScrollArea.setAutoFillBackground(True)
        self.audioScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.audioScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.audioScrollArea.setWidgetResizable(False)
        self.audioScrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.audioScrollArea.setObjectName("audioScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(10, 35, 739, 78))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.audioWidget = AudioWidget(self.scrollAreaWidgetContents)
        self.audioWidget.setGeometry(QtCore.QRect(0, -21, 731, 121))
        self.audioWidget.setObjectName("audioWidget")
        self.audioScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.speakerData = QtWidgets.QFrame(self.soundSubwindow)
        self.speakerData.setGeometry(QtCore.QRect(400, 250, 371, 281))
        self.speakerData.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.speakerData.setFrameShadow(QtWidgets.QFrame.Raised)
        self.speakerData.setObjectName("speakerData")
        self.lspeaker = QtWidgets.QLabel(self.speakerData)
        self.lspeaker.setGeometry(QtCore.QRect(0, -1, 371, 31))
        self.lspeaker.setAlignment(QtCore.Qt.AlignCenter)
        self.lspeaker.setObjectName("lspeaker")
        self.line_2 = QtWidgets.QFrame(self.speakerData)
        self.line_2.setGeometry(QtCore.QRect(0, 20, 371, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.saveButton = QtWidgets.QPushButton(self.speakerData)
        self.saveButton.setGeometry(QtCore.QRect(20, 240, 113, 32))
        self.saveButton.setObjectName("saveButton")
        self.changeButton = QtWidgets.QPushButton(self.speakerData)
        self.changeButton.setGeometry(QtCore.QRect(130, 240, 113, 32))
        self.changeButton.setObjectName("changeButton")
        self.tabWidget = QtWidgets.QTabWidget(self.speakerData)
        self.tabWidget.setGeometry(QtCore.QRect(20, 40, 331, 191))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lcountry = QtWidgets.QLabel(self.tab)
        self.lcountry.setGeometry(QtCore.QRect(10, 70, 131, 16))
        self.lcountry.setObjectName("lcountry")
        self.city = QtWidgets.QLineEdit(self.tab)
        self.city.setGeometry(QtCore.QRect(160, 40, 161, 21))
        self.city.setObjectName("city")
        self.fullname = QtWidgets.QLineEdit(self.tab)
        self.fullname.setGeometry(QtCore.QRect(160, 10, 161, 21))
        self.fullname.setObjectName("fullname")
        self.lcity = QtWidgets.QLabel(self.tab)
        self.lcity.setGeometry(QtCore.QRect(10, 40, 131, 16))
        self.lcity.setObjectName("lcity")
        self.lfullname = QtWidgets.QLabel(self.tab)
        self.lfullname.setGeometry(QtCore.QRect(10, 10, 131, 16))
        self.lfullname.setObjectName("lfullname")
        self.country = QtWidgets.QLineEdit(self.tab)
        self.country.setGeometry(QtCore.QRect(160, 70, 161, 21))
        self.country.setObjectName("country")
        self.nativelanguage = QtWidgets.QLineEdit(self.tab)
        self.nativelanguage.setGeometry(QtCore.QRect(160, 100, 161, 21))
        self.nativelanguage.setObjectName("nativelanguage")
        self.lnativelanguage = QtWidgets.QLabel(self.tab)
        self.lnativelanguage.setGeometry(QtCore.QRect(10, 100, 131, 16))
        self.lnativelanguage.setObjectName("lnativelanguage")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.accentCheckBox = QtWidgets.QCheckBox(self.tab_2)
        self.accentCheckBox.setGeometry(QtCore.QRect(30, 10, 101, 20))
        self.accentCheckBox.setTristate(False)
        self.accentCheckBox.setObjectName("accentCheckBox")
        self.disordersCheckBox = QtWidgets.QCheckBox(self.tab_2)
        self.disordersCheckBox.setGeometry(QtCore.QRect(30, 40, 161, 20))
        self.disordersCheckBox.setChecked(True)
        self.disordersCheckBox.setTristate(False)
        self.disordersCheckBox.setObjectName("disordersCheckBox")
        self.disordersSettings = QtWidgets.QFrame(self.tab_2)
        self.disordersSettings.setGeometry(QtCore.QRect(30, 60, 261, 101))
        self.disordersSettings.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.disordersSettings.setFrameShadow(QtWidgets.QFrame.Raised)
        self.disordersSettings.setObjectName("disordersSettings")
        self.disordersList = QtWidgets.QListWidget(self.disordersSettings)
        self.disordersList.setGeometry(QtCore.QRect(6, 10, 248, 52))
        self.disordersList.setMinimumSize(QtCore.QSize(248, 52))
        self.disordersList.setMaximumSize(QtCore.QSize(16777215, 52))
        self.disordersList.setSelectionRectVisible(False)
        self.disordersList.setObjectName("disordersList")
        self.addItemButton = QtWidgets.QPushButton(self.disordersSettings)
        self.addItemButton.setGeometry(QtCore.QRect(0, 60, 131, 41))
        self.addItemButton.setMinimumSize(QtCore.QSize(131, 41))
        self.addItemButton.setAutoDefault(False)
        self.addItemButton.setDefault(False)
        self.addItemButton.setFlat(False)
        self.addItemButton.setObjectName("addItemButton")
        self.removeItemButton = QtWidgets.QPushButton(self.disordersSettings)
        self.removeItemButton.setGeometry(QtCore.QRect(130, 60, 131, 41))
        self.removeItemButton.setMinimumSize(QtCore.QSize(131, 41))
        self.removeItemButton.setObjectName("removeItemButton")
        self.disordersSettings.raise_()
        self.accentCheckBox.raise_()
        self.disordersCheckBox.raise_()
        self.tabWidget.addTab(self.tab_2, "")
        self.resetButton = QtWidgets.QPushButton(self.speakerData)
        self.resetButton.setGeometry(QtCore.QRect(240, 240, 113, 32))
        self.resetButton.setObjectName("resetButton")
        self.phonemeData = QtWidgets.QFrame(self.soundSubwindow)
        self.phonemeData.setGeometry(QtCore.QRect(20, 250, 371, 281))
        self.phonemeData.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.phonemeData.setFrameShadow(QtWidgets.QFrame.Raised)
        self.phonemeData.setObjectName("phonemeData")
        self.lphoneme = QtWidgets.QLabel(self.phonemeData)
        self.lphoneme.setGeometry(QtCore.QRect(0, -1, 371, 31))
        self.lphoneme.setAlignment(QtCore.Qt.AlignCenter)
        self.lphoneme.setObjectName("lphoneme")
        self.timeStart = QtWidgets.QTimeEdit(self.phonemeData)
        self.timeStart.setGeometry(QtCore.QRect(120, 80, 118, 24))
        self.timeStart.setWrapping(False)
        self.timeStart.setFrame(True)
        self.timeStart.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.timeStart.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.timeStart.setAccelerated(False)
        self.timeStart.setCurrentSection(QtWidgets.QDateTimeEdit.SecondSection)
        self.timeStart.setCurrentSectionIndex(2)
        self.timeStart.setObjectName("timeStart")
        self.timeEnd = QtWidgets.QTimeEdit(self.phonemeData)
        self.timeEnd.setGeometry(QtCore.QRect(120, 110, 118, 24))
        self.timeEnd.setCurrentSection(QtWidgets.QDateTimeEdit.SecondSection)
        self.timeEnd.setCurrentSectionIndex(2)
        self.timeEnd.setObjectName("timeEnd")
        self.lnotation = QtWidgets.QLabel(self.phonemeData)
        self.lnotation.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.lnotation.setObjectName("lnotation")
        self.lbegin = QtWidgets.QLabel(self.phonemeData)
        self.lbegin.setGeometry(QtCore.QRect(10, 80, 101, 16))
        self.lbegin.setObjectName("lbegin")
        self.lend = QtWidgets.QLabel(self.phonemeData)
        self.lend.setGeometry(QtCore.QRect(10, 110, 101, 16))
        self.lend.setObjectName("lend")
        self.llanguage = QtWidgets.QLabel(self.phonemeData)
        self.llanguage.setGeometry(QtCore.QRect(10, 160, 101, 21))
        self.llanguage.setObjectName("llanguage")
        self.line = QtWidgets.QFrame(self.phonemeData)
        self.line.setGeometry(QtCore.QRect(0, 20, 371, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.notation = QtWidgets.QLineEdit(self.phonemeData)
        self.notation.setGeometry(QtCore.QRect(120, 40, 113, 21))
        self.notation.setObjectName("notation")
        self.addPhonemeButton = QtWidgets.QPushButton(self.phonemeData)
        self.addPhonemeButton.setGeometry(QtCore.QRect(100, 240, 171, 32))
        self.addPhonemeButton.setObjectName("addPhonemeButton")
        self.language = QtWidgets.QLineEdit(self.phonemeData)
        self.language.setGeometry(QtCore.QRect(120, 160, 113, 21))
        self.language.setObjectName("language")
        self.ldialect = QtWidgets.QLabel(self.phonemeData)
        self.ldialect.setGeometry(QtCore.QRect(10, 190, 101, 21))
        self.ldialect.setObjectName("ldialect")
        self.dialect = QtWidgets.QLineEdit(self.phonemeData)
        self.dialect.setGeometry(QtCore.QRect(120, 190, 113, 21))
        self.dialect.setObjectName("dialect")
        self.loadDataButton = QtWidgets.QPushButton(self.soundSubwindow)
        self.loadDataButton.setGeometry(QtCore.QRect(260, 540, 281, 41))
        self.loadDataButton.setMinimumSize(QtCore.QSize(281, 41))
        self.loadDataButton.setMaximumSize(QtCore.QSize(281, 41))
        self.loadDataButton.setObjectName("loadDataButton")
        self.fileSubwindow = QtWidgets.QFrame(self.centralwidget)
        self.fileSubwindow.setGeometry(QtCore.QRect(0, 10, 781, 71))
        self.fileSubwindow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fileSubwindow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fileSubwindow.setObjectName("fileSubwindow")
        self.lfile = QtWidgets.QLabel(self.fileSubwindow)
        self.lfile.setGeometry(QtCore.QRect(10, 40, 111, 21))
        self.lfile.setObjectName("lfile")
        self.currentFileName = QtWidgets.QLineEdit(self.fileSubwindow)
        self.currentFileName.setGeometry(QtCore.QRect(120, 40, 551, 21))
        self.currentFileName.setReadOnly(True)
        self.currentFileName.setObjectName("currentFileName")
        self.loadFileButton = QtWidgets.QPushButton(self.fileSubwindow)
        self.loadFileButton.setGeometry(QtCore.QRect(260, 0, 281, 41))
        self.loadFileButton.setMinimumSize(QtCore.QSize(281, 41))
        self.loadFileButton.setMaximumSize(QtCore.QSize(281, 41))
        self.loadFileButton.setObjectName("loadFileButton")
        self.fileSubwindow.raise_()
        self.soundSubwindow.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.zoomInButton.setText(_translate("MainWindow", "+"))
        self.stopButton.setText(_translate("MainWindow", "◾"))
        self.zoomOutButton.setText(_translate("MainWindow", "-"))
        self.playButton.setText(_translate("MainWindow", "▶"))
        self.lspeaker.setText(_translate("MainWindow", "Описание диктора"))
        self.saveButton.setText(_translate("MainWindow", "Сохранить"))
        self.changeButton.setText(_translate("MainWindow", "Изменить"))
        self.lcountry.setText(_translate("MainWindow", "Страна"))
        self.lcity.setText(_translate("MainWindow", "Город"))
        self.lfullname.setText(_translate("MainWindow", "Полное имя"))
        self.lnativelanguage.setText(_translate("MainWindow", "Родной язык"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Основная инормация"))
        self.accentCheckBox.setText(_translate("MainWindow", "Есть акцент"))
        self.disordersCheckBox.setText(_translate("MainWindow", "Есть дефекты речи"))
        self.addItemButton.setText(_translate("MainWindow", "Добавить"))
        self.removeItemButton.setText(_translate("MainWindow", "Удалить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Особенности речи"))
        self.resetButton.setText(_translate("MainWindow", "Сбросить"))
        self.lphoneme.setText(_translate("MainWindow", "Характеристики фонемы"))
        self.timeStart.setDisplayFormat(_translate("MainWindow", "hh:mm:ss.zzz"))
        self.timeEnd.setDisplayFormat(_translate("MainWindow", "hh:mm:ss.zzz"))
        self.lnotation.setText(_translate("MainWindow", "Обозначение"))
        self.lbegin.setText(_translate("MainWindow", "Начало"))
        self.lend.setText(_translate("MainWindow", "Конец"))
        self.llanguage.setText(_translate("MainWindow", "Язык"))
        self.addPhonemeButton.setText(_translate("MainWindow", "Добавить фонему"))
        self.ldialect.setText(_translate("MainWindow", "Диалект"))
        self.loadDataButton.setText(_translate("MainWindow", "Загрузить данные"))
        self.lfile.setText(_translate("MainWindow", "Текущий файл"))
        self.loadFileButton.setText(_translate("MainWindow", "Загрузить запись"))

from AudioWidget import AudioWidget
