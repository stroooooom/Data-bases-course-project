import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea
from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5 import QtGui


class AudioWidget(QWidget):
    __NotChangingSelectPos = 0
    __ChangingLeftSelectPos = 1
    __ChangingRightSelectPos = 2

    ZoomIn = 0
    ZoomOut = 1

    def __init__(self):
        super().__init__()
        # waveform image
        self.__origimage = QPixmap("test.png")
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

    def __getChangingSelectionPos(self, curx):
        if abs(curx - self.__startPos) < 4:
            self.__changingSelectPos = AudioWidget.__ChangingLeftSelectPos
        elif abs(curx - self.__endPos) < 4:
            self.__changingSelectPos = AudioWidget.__ChangingRightSelectPos
        else:
            self.__changingSelectPos = AudioWidget.__NotChangingSelectPos
            if curx < self.__startPos or curx > self.__endPos:
                self.resetSelection()

    def setSelectionPos(self, x):
        if self.__startPos is None:
            self.__startPos = x
            if self.__endPos is None:
                return
        if self.__endPos is None:
            self.__endPos = x
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

    def __drawOverlay(self, start, end):
        if start == end:
            return
        overlay = QPixmap(end - start, self.__curimage.height())
        overlay.fill(QColor(255, 255, 0, 50))

        self.__previmage = QPixmap(self.__curimage)
        painter = QPainter(self.__curimage)
        painter.drawPixmap(start, 0, overlay)
        self.repaint()

    def selectInterval(self):
        self.__unscaledPositions = (self.__startPos/self.__scaleRatio,
                                    self.__endPos/self.__scaleRatio)
        self.__drawOverlay(self.__startPos, self.__endPos)
        self.intervalSelected = True

    def resetSelection(self):
        self.__curimage = QPixmap(self.__previmage)
        self.intervalSelected = False
        self.__startPos = None
        self.__endPos = None
        self.repaint()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        QPainter(self).drawPixmap(0, 0, self.__curimage)

    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None:
        if not self.intervalSelected:
            self.setSelectionPos(a0.localPos().x())
        else:
            self.__getChangingSelectionPos(a0.localPos().x())

    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None:
        if self.__changingSelectPos == AudioWidget.__NotChangingSelectPos:
            return

        if self.__changingSelectPos == AudioWidget.__ChangingLeftSelectPos:
            self.__startPos = None
        else:
            self.__endPos = None

        self.__curimage = QPixmap(self.__previmage)
        self.setSelectionPos(a0.localPos().x())

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == Qt.Key_D:
            self.__resizeImage(AudioWidget.ZoomIn)
        elif a0.key() == Qt.Key_A:
            self.__resizeImage(AudioWidget.ZoomOut)

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
        if self.intervalSelected:
            self.__drawOverlay(self.__startPos, self.__endPos)
        else:
            self.repaint()

    # user API
    # def setAudio(self, filename): return
    # def __convertToTime(self): return

if __name__ == "__main__":
	app = QApplication([])
	widget = AudioWidget()

	window = QScrollArea()
	window.setFixedSize(400, 160)
	window.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

	window.setWidget(widget)
	window.show()

	sys.exit(app.exec())
