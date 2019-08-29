from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea
from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5 import QtGui
from time import strftime, gmtime
import sys


def secondsToTimeString(timeSeconds: float):
    ms = '%0.3f' % (timeSeconds % 1)
    hms = strftime('%H:%M:%S', gmtime(timeSeconds))
    return hms + ms[1:]


class AudioWidget(QWidget):
    __NotChangingSelectPos = 0
    __ChangingLeftSelectPos = 1
    __ChangingRightSelectPos = 2

    ZoomIn = 0
    ZoomOut = 1

    intervalSelectedSignal = pyqtSignal(tuple)
    resetSelectionSignal = pyqtSignal()

    def __init__(self, waveformFileName=None, duration=None):
        super().__init__()
        self.__initialised = False
        if waveformFileName and duration:
            self.init(waveformFileName, duration)

    def __getChangingSelectionPos(self, curx):
        # print(":: __getChangingSelectionPos\n",
        #       "Diff with pos1 / pos2: ",
        #       abs(curx - self.__startPos), " / ", abs(curx - self.__endPos))
        if abs(curx - self.__startPos) < 4:
            self.__changingSelectPos = AudioWidget.__ChangingLeftSelectPos
            # print("> _changingLeftSelectPos: ", abs(curx - self.__startPos))
        elif abs(curx - self.__endPos) < 4:
            self.__changingSelectPos = AudioWidget.__ChangingRightSelectPos
            # print("> _changingRightSelectPos: ", abs(curx - self.__endPos))
        else:
            # print("> __notChangingSelectPos")
            self.__changingSelectPos = AudioWidget.__NotChangingSelectPos
            if curx < self.__startPos or curx > self.__endPos:
                self.resetSelection()

    def __resetOverlay(self):
        self.__curimage = QPixmap(self.__previmage)
        self.repaint()

    def __drawOverlay(self, start, end):
        if start == end:
            return
        # print(":: __drawOverlay")
        overlay = QPixmap(end - start, self.__curimage.height())
        overlay.fill(QColor(255, 255, 0, 50))

        self.__previmage = QPixmap(self.__curimage)
        painter = QPainter(self.__curimage)
        painter.drawPixmap(start, 0, overlay)
        self.repaint()

    def __resizeImage(self, mode):
        scaleStep = 1
        if mode == AudioWidget.ZoomIn:
            if self.__scaleRatio < 10:
                self.__scaleRatio += scaleStep
        if mode == AudioWidget.ZoomOut:
            if self.__scaleRatio > 1:
                self.__scaleRatio -= scaleStep
        if self.intervalSelected:
            self.__startPos = self.__unscaledPositions[0] * self.__scaleRatio
            self.__endPos = self.__unscaledPositions[1] * self.__scaleRatio
        width = self.__origimage.width() * self.__scaleRatio
        image = QPixmap(self.__origimage)
        image = image.scaled(width, self.__curimage.height(), Qt.IgnoreAspectRatio)
        self.__curimage = image
        self.setFixedSize(image.size())
        print("pos: ", self.__startPos, self.__endPos)
        if self.intervalSelected:
            self.__drawOverlay(self.__startPos, self.__endPos)
        else:
            self.repaint()

    def __getTimeFromPos(self, xpos):  # TODO: отслеживать длительность дорожки выше в классе ?
        t = xpos / self.__curimage.width() * self.duration
        if t > 86400:
            raise ValueError("Time value is too big")
        return secondsToTimeString(t)

    def __getPosFromTime(self, time):
        pos = time / self.duration * self.__curimage.width()
        return pos

    def init(self, waveformFileName, duration):
        self.__initialised = True
        self.filename = waveformFileName
        self.duration = duration
        # waveform image
        self.__origimage = QPixmap(self.filename)
        self.__previmage = QPixmap(self.__origimage)
        self.__curimage = QPixmap(self.__origimage)
        self.__scaleRatio = 1
        # selection overlay
        self.__unscaledPositions = None
        self.__startPos = None
        self.__endPos = None
        self.__changingSelectPos = AudioWidget.__NotChangingSelectPos
        self.intervalSelected = False

        self.setFixedSize(self.__origimage.size())
        self.setFocusPolicy(Qt.StrongFocus)
        self.repaint()

    def changeStartPos(self, timeSeconds):
        self.__startPos = self.__getPosFromTime(timeSeconds)
        if self.__endPos:
            self.__resetOverlay()
            self.selectInterval()

    def changeEndPos(self, timeSeconds):
        self.__endPos = self.__getPosFromTime(timeSeconds)
        if self.__startPos:
            self.__resetOverlay()
            self.selectInterval()

    def setSelectionPos(self, xpos):
        # print(":: setSelectionPoint")
        if self.__startPos is None:
            self.__startPos = xpos
            if self.__endPos is None:
                return
        if self.__endPos is None:
            self.__endPos = xpos
            if self.__startPos is None:
                return
        if self.__endPos < self.__startPos:
            self.__startPos, self.__endPos = self.__endPos, self.__startPos
            if self.__changingSelectPos:
                # Next operation changes selectPosition, which we are moving.
                # If __endPos is to the left of the __startPos, user begins
                # moving __startPos instead of keeping moving __endPos
                self.__changingSelectPos = (self.__changingSelectPos % 2) + 1
        self.selectInterval()

    def selectInterval(self):
        if not self.__startPos or not self.__endPos:
            raise AssertionError("Selected less than 2 positions")
        self.__unscaledPositions = (self.__startPos / self.__scaleRatio,
                                    self.__endPos / self.__scaleRatio)
        self.intervalSelected = True
        self.__drawOverlay(self.__startPos, self.__endPos)
        # print("start/end poss: ", self.__startPos, " / ", self.__endPos)
        self.intervalSelectedSignal.emit(self.getTimeInterval())

    def resetSelection(self):
        self.__resetOverlay()
        self.intervalSelected = False
        self.__startPos = None
        self.__endPos = None
        self.resetSelectionSignal.emit()

    def zoomIn(self):
        self.__resizeImage(AudioWidget.ZoomIn)

    def zoomOut(self):
        self.__resizeImage(AudioWidget.ZoomOut)

    def getTimeInterval(self):
        if not self.intervalSelected:
            startTime, endTime = self.__getTimeFromPos(0), self.__getTimeFromPos(0)
        else:
            startTime = self.__getTimeFromPos(self.__startPos)
            endTime = self.__getTimeFromPos(self.__endPos)
        return startTime, endTime

    def getDurationTime(self):
        return secondsToTimeString(self.duration)


    # QWidget overloaded methods
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        if self.__initialised:
            painter = QPainter(self)
            painter.drawPixmap(0, 0, self.__curimage)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        # print("\n\n:: mousePressEvent!")
        # print("> intervalSelected: ", self.intervalSelected)
        if not self.intervalSelected:
            # print("> calling setSelectionPoint")
            self.setSelectionPos(a0.localPos().x())
        else:
            # print("> calling __getChangingSelectionPos")
            self.__getChangingSelectionPos(a0.localPos().x())

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        # print("\n\n:: mouseMoveEvent!")
        if self.__changingSelectPos == AudioWidget.__NotChangingSelectPos:
            return

        # print("> changing select pos")
        if self.__changingSelectPos == AudioWidget.__ChangingLeftSelectPos:
            self.__startPos = None
            # print(">> leftSelectPos reset")
        else:
            self.__endPos = None
            # print(">> rightSelectPos reset")

        self.__curimage = QPixmap(self.__previmage)
        self.setSelectionPos(a0.localPos().x())

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        # print("\n\n:: keyPressEvent!")
        if a0.key() == Qt.Key_D:
            # print("> ZoomIn")
            self.__resizeImage(AudioWidget.ZoomIn)
        elif a0.key() == Qt.Key_A:
            # print("> ZoomOut")
            self.__resizeImage(AudioWidget.ZoomOut)


if __name__ == '__main__':
    app = QApplication([])
    widget = AudioWidget()

    window = QScrollArea()
    window.setFixedSize(400, 160)
    window.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    window.setWidget(widget)
    window.show()

    sys.exit(app.exec())
