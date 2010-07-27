
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_ActionWidget			import Ui_Action
from editActionDialogHandler	import editActionDialogHandler

class actionHandler(QWidget):
	'''
	Handler for the action object
	'''
	def __init__(self, parent, action):
		'''
		Initializes the action object
		'''
		QWidget.__init__(self, parent)
		self.actionHandler = Ui_Action()
		self.actionHandler.setupUi(self)
		self.setAttribute(Qt.WA_DeleteOnClose)
		
		self.parent = parent
		# parent branch list for modifyActionWidget uses
		self.actions = self.parent.actions
		self.action = action
		self.parent.actions.append(self.action)
		self.setName(self.action.type, self.action.values)
		
	def setName(self, type, values):
		'''
		Sets the text on the main button with the type and value(s)
		'''
		self.actionHandler.editButton.setText(str(type) + ": " + str(values))
		
	def modifyActionWidget(self, type, values):
		'''
		Edits the action widget's type and values information
		'''
		self.action.type = type
		self.action.values = values
		self.setName(self.action.type, self.action.values)
		
	'''
	SIGNALS/SLOTS
	'''
	def editAction(self):
		'''
		Opens a dialog window to edit the action object and wrapper object
		'''
		self.actionDialog = editActionDialogHandler(self)
		# sets the type and values to current values
		self.actionDialog.setName(self.action.type, self.action.values)
		self.actionDialog.show()
		
	def deleteAction(self):
		'''
		Deletes the action object and closes the wrapper object
		'''
		self.parent.removeActionWidget(self)