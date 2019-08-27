from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QFileDialog
# from PyQt5.QtCore.QMetaType import QString

'''
palette = QtGui.QPalette()
brush = QtGui.QBrush(QtGui.QColor(33, 255, 6))
brush.setStyle(QtCore.Qt.SolidPattern)
palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
'''

# Импортируем нашу форму.
from ui_beta import Ui_MainWindow
import sys
# import entity
from Graph import Entity


class MyWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MyWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.init_connections()
		self.checkDisordersSettings()

	def init_connections(self):
		self.ui.saveButton.clicked.connect(self.getSpeakerSettings)
		self.ui.saveButton.clicked.connect(self.disableSpeakerSettings)

		self.ui.disordersList.doubleClicked.connect(self.edition)
		self.ui.changeButton.clicked.connect(self.enableSpeakerSettings)
		self.ui.loadFileButton.clicked.connect(self.loadFile)

		self.ui.disordersCheckBox.stateChanged.connect(self.checkDisordersSettings)

		# self.ui.audioviz.

		return

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

	def edition(self): #TODO rename
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
		begin = self.ui.timeBegin.text()
		end = self.ui.timeEnd.text()
		language = self.ui.language_list.currentText()

		try:
			phoneme = Entity.Phoneme(notation, begin, end, language)
		except ValueError as exception:
			print("ValueError occurred: ", str(exception))
		# pass
		# ...
		else:
			return phoneme

		return [notation, begin, end, language]

	def loadFile(self):
		filename = QFileDialog.getOpenFileName(self)[0]
		print("Filename: ", filename)

		self.ui.currentFileName.setText(filename)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
