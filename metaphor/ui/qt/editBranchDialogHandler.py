
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_EditBranchDialog import Ui_EditBranchDialog

class editBranchDialogHandler(QWidget):
	'''
	Handler for the branch object
	'''
	def __init__(self, parent):
		'''
		Initializes the branch object
		'''
		QWidget.__init__(self)
		self.dialog = Ui_EditBranchDialog()
		self.dialog.setupUi(self)
		self.parent = parent
		self.name = ""
		
	def setName(self, name, weight):
		'''
		Presets the name and weight inside the dialog
		'''
		self.name = str(name)
		self.dialog.nameInput.setText(name)
		self.dialog.weightInput.setValue(weight)
		
	def presetNameOnly(self, name):
		self.dialog.nameInput.setText(name)
		
	'''
	SIGNALS/SLOTS
	'''
	def accept(self):
		'''
		OK: edit the name and weight with new values
		'''
		name = self.dialog.nameInput.text()
		weight = self.dialog.weightInput.value()
		tempName = name		# store the name temporarily
		count = 0			# start a count for the name
		# loop through all the branches
		keepLoop = True
		while keepLoop:
			keepLoop = False
			# check if current branch name is already taken
			for bran in self.parent.branches:
				# if name is unchanged, break loop
				if tempName == self.name:
					break
				# if name is already taken, append a number
				if tempName == bran.name:
					count += 1
					tempName = name + str(count)
					keepLoop = True
		name = tempName		# temporary name gets passed
		self.parent.modifyBranchWidget(name, weight)
		self.close()
		
	def reject(self):
		'''
		Cancel: Close dialog
		'''
		self.close()