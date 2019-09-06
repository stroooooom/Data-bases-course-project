from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui_app2 import Ui_MainWindow
import sys
import os

from GraphAPI import Graph
import wave
from SoundRecord import SoundRecord, SoundCombiner


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.__graph = Graph.Driver()
        self.__soundRecords = None
        self.__currentRecord = None

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Coursache")

        self.init_connections()

    def init_connections(self):
        self.ui.matchButton.clicked.connect(self.match)
        self.ui.playButton.clicked.connect(self.play)
        self.ui.stopButton.clicked.connect(self.stop)

    def play(self):
        if self.__currentRecord and self.__currentRecord.isPlaying():
            self.__currentRecord.stop()
        id = self.ui.soundList.currentRow()
        self.__currentRecord = self.__soundRecords[id]
        self.__currentRecord.play()

    def stop(self):
        if self.__currentRecord:
            self.__currentRecord.stop()

    def match(self):
        if not self.ui.word.text():
            QMessageBox.warning(self, None, "Строка со словом не должна быть пустой")
            return
        self.__deleteFiles()
        self.__soundRecords = list()
        word = self.ui.word.text()
        self.__graph.getQuery.setWord(word)
        result = self.__graph.getData()
        for data in result:
            filename = self.__createSound(word, data)
            self.ui.soundList.addItem(filename)
            self.ui.soundList.repaint()
            self.__soundRecords.append(SoundRecord(filename))
        self.ui.soundList.repaint()

    def __createSound(self, word, data: dict):
        wavfile = wave.open(data['filePath'], 'rb')
        filename = data['name'] + "_pronounced_word.wav"
        comb = SoundCombiner()
        comb.create(filename)
        for i in range(len(word)):
            time = data[word[i]]
            comb.join(wavfile, time[0], time[1])
        comb.detach()
        return filename

    def __deleteFiles(self):
        for i in range(self.ui.soundList.count()-1, -1, -1):
            item = self.ui.soundList.takeItem(i).text()
            os.remove(item)

    def close(self):
        self.__deleteFiles()


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
app.aboutToQuit.connect(application.close)

sys.exit(app.exec())
