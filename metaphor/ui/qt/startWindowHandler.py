
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import glob

from Ui_StartWindow import Ui_StartWindow

class startWindowHandler(QWidget):
	'''
	Handler for the start window
	'''
	def __init__(self, parent, recentFiles, sampleDir):
		'''
		Initializes the start window
		'''
		QWidget.__init__(self)
		self.startWindow = Ui_StartWindow()
		self.startWindow.setupUi(self)
		self.recentFiles = recentFiles
		self.sampleDir = sampleDir
		
		self.parent = parent
		
		self.getRecentFiles()
		self.generateSampleList()

	def getRecentFiles(self):
		'''
		Generate recent file buttons based on recent file list
		'''
		listRecent = open(self.recentFiles)
		for line in listRecent:
			button = QToolButton(self)
			buttonAction = QAction(button)
			buttonAction.setData(file)
			button.setDefaultAction(buttonAction)
			button.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed))
			button.setMaximumSize(QSize(16777215, 20))
			button.setText(line[line.rfind("/")+1:len(line)].strip())
			button.setToolTip(QApplication.translate("StartWindow", "Open " + line, None, QApplication.UnicodeUTF8))
			button.setStatusTip(QApplication.translate("StartWindow", "Open " + line, None, QApplication.UnicodeUTF8))
			self.startWindow.openLayout.insertWidget(2, button)
			self.connect(button, SIGNAL("triggered(QAction*)"), self.openFromButton)
		listRecent.close()
			
	def generateSampleList(self):
		'''
		Generate sample buttons based on files in sample directory
		'''
		listFiles = glob.glob(self.sampleDir + "*.xml")
		for file in listFiles:
			button = QToolButton(self)
			buttonAction = QAction(button)
			buttonAction.setData(file)
			button.setDefaultAction(buttonAction)
			button.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed))
			button.setMaximumSize(QSize(16777215, 20))
			button.setText(file[file.rfind("/")+1:len(file)].strip())
			button.setToolTip(QApplication.translate("StartWindow", "Open " + file, None, QApplication.UnicodeUTF8))
			button.setStatusTip(QApplication.translate("StartWindow", "Open " + file, None, QApplication.UnicodeUTF8))
			self.startWindow.sampleLayout.insertWidget(2, button)
			self.connect(button, SIGNAL("triggered(QAction*)"), self.openFromButton)
	'''
	SIGNALS/SLOTS
	'''
	def openFile(self):
		'''
		Opens a open new file dialog
		'''
		if self.parent.openFile():
			self.close()
			
	def openFromButton(self, buttonAction):
		'''
		Opens the file based on the button's text
		'''
		if self.parent.loadFile(buttonAction.data().toString()):
			self.close()
			
	def newTurtle(self):
		if self.parent.newTurtle():
			self.close()
			
	def newBranch3D(self):
		if self.parent.newBranch3D():
			self.close()
			
	def newDla3D(self):
		if self.parent.newDla3D():
			self.close()