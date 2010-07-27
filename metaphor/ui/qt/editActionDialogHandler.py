
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import random

from Ui_EditActionDialog import Ui_EditActionDialog

class editActionDialogHandler(QWidget):
	'''
	Handler for the Action object
	'''
	def __init__(self, parent):
		'''
		Initializes the Action object
		'''
		QWidget.__init__(self)
		self.dialog = Ui_EditActionDialog()
		self.dialog.setupUi(self)
		self.parent = parent
		self.name = ""
		
	def setName(self, name, values):
		'''
		Presets the type and values inside the dialog
		'''
		self.name = str(name)
		#self.dialog.nameInput.setText(name)
		#self.dialog.weightInput.setValue(weight)
		
	'''
	SIGNALS/SLOTS
	'''
	def accept(self):
		'''
		OK: edit type and values with new values
		'''
		# find action type
		# load extra horizontal layouts with a label and a spinbox
		# save type as type and spinbox values into values array
		type = "TYPE" + str(random.random())
		values = ["VALUE1", "VALUE2", "VALUE3"]
		# send information to parent (branch)
		self.parent.modifyActionWidget(type, values)
		self.close()
		
	def reject(self):
		'''
		Cancel: Close dialog
		'''
		self.close()