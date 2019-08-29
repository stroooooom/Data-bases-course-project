from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QDateTime, QTime
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QFileDialog, QScrollBar

# from PyQt5.QtCore.QMetaType import QString
# import time
from WaveGraph import SoundRecord

'''
palette = QtGui.QPalette()
brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
'''

# TODO: Добавить полосу на графе, соотвествующую текущему времени вопроизведения
# TODO: Заменить принты всплывающим окном с предупреждением/cообщением об ошибке
# TODO: Клиентская часть должна проверять валидность введенной информации (которая затем будет в запросе)

# Импортируем форму
from ui_beta import Ui_MainWindow
import sys
from Graph import Entity
from AudioWidget import AudioWidget


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.speechRecord = None
        self.__recordDuration = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.audioScrollArea.setWidget(self.ui.audioWidget)
        self.checkDisordersSettings()
        self.init_connections()
        for widget in self.ui.soundSubwindow.children():
            widget.blockSignals(True)

    def init_connections(self):
        self.ui.disordersList.doubleClicked.connect(self.edition)
        self.ui.disordersCheckBox.stateChanged.connect(self.checkDisordersSettings)
        self.ui.audioWidget.intervalSelectedSignal.connect(self.setSelection)
        self.ui.audioWidget.resetSelectionSignal.connect(self.resetSelection)
        self.ui.saveButton.clicked.connect(self.getSpeakerSettings)
        self.ui.saveButton.clicked.connect(self.disableSpeakerSettings)
        self.ui.changeButton.clicked.connect(self.enableSpeakerSettings)
        self.ui.loadFileButton.clicked.connect(self.loadFile)
        self.ui.zoomInButton.clicked.connect(self.zoomIn)
        self.ui.zoomOutButton.clicked.connect(self.zoomOut)
        self.ui.playButton.clicked.connect(self.playAudio)
        self.ui.stopButton.clicked.connect(self.stopAudio)
        self.ui.timeStart.timeChanged.connect(self.changedTimeStart)
        self.ui.timeEnd.userTimeChanged.connect(self.changedTimeEnd)

    def checkDisordersSettings(self):
        checked = self.ui.disordersCheckBox.isChecked()
        if checked:
            self.ui.disordersSettings.setDisabled(False)
        else:
            self.ui.disordersSettings.setDisabled(True)

    def disableSpeakerSettings(self):
        self.ui.tabWidget.setDisabled(True)
        self.ui.tabWidget.repaint()

    def enableSpeakerSettings(self):
        self.ui.tabWidget.setDisabled(False)
        self.ui.tabWidget.repaint()

    def edition(self):  # TODO rename
        print("edition called")
        self.ui.disordersList.currentItem().setFlags(Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.ui.disordersList.clearSelection()

    def getSpeakerSettings(self):
        fullname = self.ui.fullname.text()
        city = self.ui.city.text()
        country = self.ui.country.text()
        native_language = self.ui.nativelanguage.text()
        accent = self.ui.accentCheckBox.isChecked()
        disorders = []
        if self.ui.disordersCheckBox.isChecked():
            for i in range(self.ui.disordersList.count()):
                item = self.ui.disordersList.item(i)
                if item:
                    disorders.append(item)

        try:
            speaker = Entity.Person(fullname, native_language, city, country,
                                    accent, disorders)
        except ValueError as exception:
            print("ValueError occurred: ", str(exception))
        # pass
        # вызов сообщения с предупреждением
        else:
            return speaker

    def getPhonemeDescription(self):
        notation = self.ui.notation.text()
        start = self.ui.timeStart.text()
        end = self.ui.timeEnd.text()
        language = self.ui.language_list.currentText()

        try:
            phoneme = Entity.Phoneme(notation, start, end, language)
        except ValueError as exception:
            print("ValueError occurred: ", str(exception))
        # pass
        # ...
        else:
            return phoneme

        return [notation, start, end, language]

    def loadFile(self):
        filename = QFileDialog.getOpenFileName(self)[0]
        self.ui.currentFileName.setText(filename)
        try:
            self.speechRecord = SoundRecord(filename)
            picture = self.speechRecord.getWaveformPicture()
        except BaseException as tError:
            print("Error raised: ", tError)
        else:
            self.ui.audioWidget.init(picture, self.speechRecord.duration)
            self.__recordDuration = QTime.fromString(self.ui.audioWidget.getDurationTime())
            self.resetSelection()
            for widget in self.ui.soundSubwindow.children():
                widget.blockSignals(False)

    def setSelection(self, timeInterval):
        print("setSelection called")
        self.ui.timeStart.blockSignals(True)
        self.ui.timeEnd.blockSignals(True)
        self.ui.timeStart.setTime(QTime.fromString(timeInterval[0]))
        self.ui.timeEnd.setTime(QTime.fromString(timeInterval[1]))
        self.ui.timeStart.blockSignals(False)
        self.ui.timeEnd.blockSignals(False)

    def resetSelection(self):
        print("resetSelection called")
        self.ui.timeStart.blockSignals(True)
        self.ui.timeEnd.blockSignals(True)
        self.ui.timeStart.setTime(QTime(0, 0, 0, 0))
        self.ui.timeEnd.setTime(QTime(0, 0, 0, 0))
        self.ui.timeStart.blockSignals(False)
        self.ui.timeEnd.blockSignals(False)
        self.ui.timeStart.setMinimumTime(QTime(0, 0, 0, 0))
        self.ui.timeEnd.setMinimumTime(QTime(0, 0, 0, 0))
        self.ui.timeStart.setMaximumTime(self.__recordDuration)
        self.ui.timeEnd.setMaximumTime(self.__recordDuration)

    def changedTimeStart(self, time: QTime):
        print("changedTimeStart called")
        timeSeconds = time.msecsSinceStartOfDay() / 1e3
        self.ui.audioWidget.changeStartPos(timeSeconds)
        self.ui.timeEnd.setMinimumTime(self.ui.timeStart.time())

    def changedTimeEnd(self, time: QTime):
        print("changedTimeEnd called")
        timeSeconds = time.msecsSinceStartOfDay() / 1e3
        self.ui.audioWidget.changeEndPos(timeSeconds)
        self.ui.timeStart.setMaximumTime(self.ui.timeEnd.time())

    def zoomIn(self):
        print("Zoom In")
        scrollBar = self.ui.audioScrollArea.horizontalScrollBar()
        scrollPos = scrollBar.value() / scrollBar.maximum()
        self.ui.audioWidget.zoomIn()
        scrollBar.setValue(scrollPos * scrollBar.maximum())
        self.ui.audioScrollArea.update()

    def zoomOut(self):
        print("Zoom Out")
        scrollBar = self.ui.audioScrollArea.horizontalScrollBar()
        scrollPos = scrollBar.value() / scrollBar.maximum()
        self.ui.audioWidget.zoomOut()
        scrollBar.setValue(scrollPos * scrollBar.maximum())
        self.ui.audioScrollArea.update()

    def playAudio(self):
        print("Play Audio")
        start = self.ui.timeStart.time().second() + (self.ui.timeStart.time().msec()/1000)
        end = self.ui.timeEnd.time().second() + (self.ui.timeEnd.time().msec() / 1000)
        self.speechRecord.play(start, end)

    def stopAudio(self):
        print("Stop Audio")
        self.speechRecord.stop()

app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
