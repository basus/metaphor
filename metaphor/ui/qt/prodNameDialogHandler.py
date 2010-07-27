
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_ProductionNameDialog	import Ui_ProductionNameDialog

class prodNameDialogHandler(QWidget):
	'''
	Handler for the branch object
	'''
	def __init__(self, parent):
		'''
		Initializes the branch object
		'''
		QWidget.__init__(self)
		self.dialog = Ui_ProductionNameDialog()
		self.dialog.setupUi(self)
		self.parent = parent
		self.name = ""
		
	def setName(self,name):
		'''
		Presets the name inside of the dialog
		'''
		self.name = str(name)
		self.dialog.nameInput.setText(name)
		
	'''
	SIGNALS/SLOTS
	'''
	def accept(self):
		'''
		OK: edit name with new value
		'''
		# grab name from input
		name = self.dialog.nameInput.text()
		tempName = name		# store the name temporarily
		count = 0			# start a count for the name
		# loop through all the productions
		keepLoop = True
		while keepLoop:
			keepLoop = False
			# check if current branch name is already taken
			for prod in self.parent.productions:
				# if name is unchanged, break loop
				if tempName == self.name:
					break
				# if name is already taken, append a number
				if tempName == prod.name:
					count += 1
					tempName = name + str(count)
					keepLoop = True
		name = tempName		# temporary name gets passed
		self.parent.modifyProductionWidget(name)
		# show add axiom button if there is at least one production
		if self.parent.productions:
			if self.parent.ui.axiomList.isHidden():
				self.parent.ui.addAxiom.show()
				self.parent.ui.axiomList.hide()
			else:
				self.parent.ui.addAxiom.hide()
				self.parent.ui.axiomList.clear()
				for production in self.parent.productions:
					self.parent.ui.axiomList.addItem(QString(production.name))
				self.parent.ui.axiomList.show()
		self.close()
		
	def reject(self):
		'''
		Cancel: Close dialog
		'''
		self.close()