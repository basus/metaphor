
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_GenerateDialog import Ui_GenerateDialog

class generateDialogHandler(QWidget):
	'''
	Handler for the Action object
	'''
	def __init__(self, parent):
		'''
		Initializes the Action object
		'''
		QWidget.__init__(self)
		self.dialog = Ui_GenerateDialog()
		self.dialog.setupUi(self)
		
		self.parent = parent
		
	'''
	SIGNALS/SLOTS
	'''
	def accept(self):
		genValue = self.dialog.generations.value()
		self.parent.drawImage(genValue)
		self.close()
		
	def reject(self):
		print "close"
		self.close()