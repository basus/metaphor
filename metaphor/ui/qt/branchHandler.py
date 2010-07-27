
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from grammarPieces				import Action
from Ui_BranchWidget			import Ui_Branch
from editBranchDialogHandler	import editBranchDialogHandler
from actionHandler				import actionHandler
from editActionDialogHandler	import editActionDialogHandler

class branchHandler(QWidget):
	'''
	Handler for the branch object
	'''
	def __init__(self, parent, branch):
		'''
		Initializes the branch object
		'''
		QWidget.__init__(self, parent)
		self.branchHandler = Ui_Branch()
		self.branchHandler.setupUi(self)
		self.setAttribute(Qt.WA_DeleteOnClose)
		
		self.parent = parent
		# parent branch list for modifyBranchWidget uses
		self.branches = self.parent.branches
		self.branch = branch
		self.parent.branches.append(self.branch)
		self.setName(self.branch.name, self.branch.weight)
		self.actions = []
		self.countActions = 0
		
	def setName(self, name, weight):
		'''
		Sets the text on the main button with the name and weight
		'''
		self.branchHandler.nameButton.setText(str(name) + ": " + str(weight))
		
	def modifyBranchWidget(self, name, weight):
		'''
		Edits the branch widget's name and weight information
		'''
		self.branch.name = name
		self.branch.weight = weight
		self.setName(self.branch.name, self.branch.weight)
		
	def saveActions(self):
		self.branch.actions = self.actions
		
	def loadActions(self):
		'''
		Loads the branch's action objects into the layout
		'''
		self.countActions = len(self.branch.actions)
		for i in range(self.countActions):
			newActionHandler = actionHandler(self, self.branch.actions[i])
			self.branchHandler.actionsLayout.insertWidget(i, newActionHandler)
		
	def modifyActionWidget(self, type, values):
		'''
		Creates an action widget and adds it to the layout
		'''
		# create a new action object
		newAction = Action(type, values)
		# create its handler
		newActionHandler = actionHandler(self, newAction)
		# insert the handler into the layout
		self.branchHandler.actionsLayout.insertWidget(self.countActions, newActionHandler)
		# increment the count
		self.countActions += 1
				
	def removeActionWidget(self, actionHandler):
		self.actions.remove(actionHandler.action)
		self.countActions -= 1
		actionHandler.close()
		self.branchHandler.actionsLayout.removeWidget(actionHandler)
		
	'''
	SIGNALS/SLOTS
	'''
	def editName(self):
		'''
		Opens a dialog to edit the branch object and wrapper object
		'''
		self.branchDialog = editBranchDialogHandler(self)
		# sets the name and weight to current values
		self.branchDialog.setName(self.branch.name, self.branch.weight)
		self.branchDialog.show()
		
	def deleteBranch(self):
		'''
		Deletes the object and closes the wrapper object
		'''
		# remove all action widgets
		for i in range(len(self.actions)):
			layout = self.branchHandler.actionsLayout
			curAction = layout.itemAt(i).widget()
			curAction.close()
			layout.removeItem(layout.itemAt(i))
		self.parent.removeBranchWidget(self)
	
	def addAction(self):
		'''
		Opens a dialog to add an action widget to the layout
		'''
		self.actionDialog = editActionDialogHandler(self)
		self.actionDialog.show()