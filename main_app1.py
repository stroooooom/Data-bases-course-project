from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTime
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QMessageBox
from ui_app1 import Ui_MainWindow
import sys

from GraphAPI import Entity, Graph
from SoundRecord import SoundRecord


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.__graph = Graph.Driver()
        self.__speechRecord = None
        self.__recordDuration = None
        self.__speakerData = None
        self.__phonemes = list()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Coursache")
        self.ui.audioScrollArea.setWidget(self.ui.audioWidget)
        self.checkDisordersSettings()
        self.init_connections()
        for widget in self.ui.soundSubwindow.children():
            widget.blockSignals(True)

    def init_connections(self):
        self.ui.disordersList.doubleClicked.connect(self.editItemOfDisorderList)
        self.ui.disordersCheckBox.stateChanged.connect(self.checkDisordersSettings)
        self.ui.audioWidget.intervalSelectedSignal.connect(self.setSelection)
        self.ui.audioWidget.resetSelectionSignal.connect(self.resetSelection)
        self.ui.timeStart.timeChanged.connect(self.changedTimeStart)
        self.ui.timeEnd.userTimeChanged.connect(self.changedTimeEnd)

        self.ui.loadFileButton.clicked.connect(self.loadFile)

        self.ui.zoomInButton.clicked.connect(self.zoomIn)
        self.ui.zoomOutButton.clicked.connect(self.zoomOut)
        self.ui.playButton.clicked.connect(self.playAudio)
        self.ui.stopButton.clicked.connect(self.stopAudio)

        self.ui.addPhonemeButton.clicked.connect(self.addPhoneme)

        self.ui.saveButton.clicked.connect(self.savePerson)
        self.ui.changeButton.clicked.connect(self.enableSpeakerSettings)
        self.ui.resetButton.clicked.connect(self.resetSpeakerSettings)

        self.ui.addItemButton.clicked.connect(self.addItemToDisorderList)
        self.ui.removeItemButton.clicked.connect(self.removeItemFromDisorderList)

        self.ui.loadDataButton.clicked.connect(self.loadData)

    def checkDisordersSettings(self):
        checked = self.ui.disordersCheckBox.isChecked()
        self.ui.disordersSettings.setDisabled(not checked)

    def disableSpeakerSettings(self):
        self.ui.tabWidget.setDisabled(True)
        self.ui.tabWidget.repaint()

    def enableSpeakerSettings(self):
        self.ui.tabWidget.setDisabled(False)
        self.ui.tabWidget.repaint()

    def resetSpeakerSettings(self):
        self.ui.accentCheckBox.setCheckState(Qt.Unchecked)
        self.ui.fullname.clear()
        self.ui.city.clear()
        self.ui.country.clear()
        self.ui.nativelanguage.clear()
        for i in range(self.ui.disordersList.count() - 1, -1, -1):
            self.ui.disordersList.takeItem(i)
        self.ui.disordersCheckBox.setCheckState(Qt.Checked)
        self.enableSpeakerSettings()

    def addItemToDisorderList(self):
        text, ok = QInputDialog.getText(self, None, 'Введите названия нарушения:')
        if ok:
            if text:
                self.ui.disordersList.addItem(text.lower())
                self.ui.disordersList.repaint()
            else:
                QMessageBox.warning(self, None, "Название не содержит символов")

    def editItemOfDisorderList(self):
        self.ui.disordersList.currentItem().setFlags(Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        self.ui.disordersList.clearSelection()

    def removeItemFromDisorderList(self):
        self.ui.disordersList.takeItem(self.ui.disordersList.currentRow())

    def loadFile(self):
        filename = QFileDialog.getOpenFileName(self)[0]
        self.ui.currentFileName.setText(filename)
        try:
            self.speechRecord = SoundRecord(filename)
            picture = self.speechRecord.getWaveformPicture()
        except BaseException as e:
            msg = "Возникла ошибка при загрузке файла:\n" + str(e)
            QMessageBox.warning(self, None, msg)
        else:
            self.ui.audioWidget.init(picture, self.speechRecord.duration)
            self.__recordDuration = QTime.fromString(self.ui.audioWidget.getDurationTime())
            self.resetSelection()
            for widget in self.ui.soundSubwindow.children():
                widget.blockSignals(False)

    def __setTimeStart(self, time: QTime):  # blocks signals of the widget
        self.ui.timeStart.blockSignals(True)
        self.ui.timeStart.setTime(time)
        self.ui.timeStart.blockSignals(False)

    def __setTimeEnd(self, time: QTime):  # blocks signals of the widget
        self.ui.timeEnd.blockSignals(True)
        self.ui.timeEnd.setTime(time)
        self.ui.timeEnd.blockSignals(False)

    def setSelection(self, timeInterval):
        self.__setTimeStart(QTime.fromString(timeInterval[0]))
        self.__setTimeEnd(QTime.fromString(timeInterval[1]))

    def resetSelection(self):
        self.__setTimeStart(QTime(0, 0, 0, 0))
        self.__setTimeEnd(QTime(0, 0, 0, 0))
        self.ui.timeStart.setMinimumTime(QTime(0, 0, 0, 0))
        self.ui.timeEnd.setMinimumTime(QTime(0, 0, 0, 0))
        self.ui.timeStart.setMaximumTime(self.__recordDuration)
        self.ui.timeEnd.setMaximumTime(self.__recordDuration)
        self.stopAudio()

    def changedTimeStart(self, time: QTime):
        timeSeconds = time.msecsSinceStartOfDay() / 1e3
        self.ui.audioWidget.changeStartPos(timeSeconds)
        self.ui.timeEnd.setMinimumTime(self.ui.timeStart.time())

    def changedTimeEnd(self, time: QTime):
        timeSeconds = time.msecsSinceStartOfDay() / 1e3
        self.ui.audioWidget.changeEndPos(timeSeconds)
        self.ui.timeStart.setMaximumTime(self.ui.timeEnd.time())

    def zoomIn(self):
        scrollBar = self.ui.audioScrollArea.horizontalScrollBar()
        scrollPos = scrollBar.value() / scrollBar.maximum()
        self.ui.audioWidget.zoomIn()
        scrollBar.setValue(scrollPos * scrollBar.maximum())
        self.ui.audioScrollArea.update()

    def zoomOut(self):
        scrollBar = self.ui.audioScrollArea.horizontalScrollBar()
        scrollPos = scrollBar.value() / scrollBar.maximum()
        self.ui.audioWidget.zoomOut()
        scrollBar.setValue(scrollPos * scrollBar.maximum())
        self.ui.audioScrollArea.update()

    def playAudio(self):
        start = self.ui.timeStart.time().second() + (self.ui.timeStart.time().msec() / 1000)
        end = self.ui.timeEnd.time().second() + (self.ui.timeEnd.time().msec() / 1000)
        self.speechRecord.play(start, end)

    def stopAudio(self):
        self.speechRecord.stop()

    def getPhoneme(self) -> Entity.Phoneme:
        return Entity.Phoneme(
            self.ui.notation.text().lower(),
            self.ui.timeStart.text(),
            self.ui.timeEnd.text(),
            self.ui.language.text().lower(),
            self.ui.dialect.text().lower())

    def getPerson(self) -> Entity.Person:
        disorders = None
        if self.ui.disordersCheckBox.isChecked():
            disorders = [self.ui.disordersList.item(i).text().lower()
                         for i in range(self.ui.disordersList.count())
                         if self.ui.disordersList.item(i)]
        person = Entity.Person(
            self.ui.fullname.text(),
            self.ui.nativelanguage.text().lower(),
            self.ui.city.text(),
            self.ui.country.text(),
            self.ui.accentCheckBox.isChecked(),
            disorders)
        return person

    def addPhoneme(self):
        try:
            self.__phonemes.append(self.getPhoneme())
        except BaseException as e:
            msg = "Возникла ошибка при добавлении фонемы:\n"+str(e)
            QMessageBox.warning(self, None, msg)
        else:
            print("New phoneme '{}' was added to the list".format(self.__phonemes[-1].notation))
            self.ui.notation.clear()
            self.ui.notation.repaint()

    def savePerson(self):
        try:
            self.__graph.loadQuery.person = self.getPerson()
        except BaseException as e:
            msg = "Возникла ошибка при сохранении данных диктора:\n" + str(e)
            QMessageBox.warning(self, None, msg)
        else:
            self.disableSpeakerSettings()

    def loadData(self):
        if not self.ui.currentFileName.text():
            QMessageBox.warning(self, None, "Не указано имя файла")
            return
        if not self.__phonemes:
            QMessageBox.warning(self, None, "Фонемы не добавлены")
            return
        self.__graph.loadQuery.setRecord(self.ui.currentFileName.text())
        self.__graph.loadQuery.addPhonemes(self.__phonemes)
        try:
            self.__graph.loadData()
        except BaseException as e:
            msg = "Возникла ошибка при загрузке данных:\n" + str(e)
            QMessageBox.warning(self, None, msg)
        else:
            QMessageBox.information(self, None, "Данные успешно загружены")


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
