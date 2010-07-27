
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_ProductionWidget	import Ui_Production
from prodNameDialogHandler	import prodNameDialogHandler

class productionHandler(QWidget):
	'''
	Handler for the production object
	'''
	def __init__(self, parent, production):
		'''
		Initializes the production object
		'''
		QWidget.__init__(self, parent)
		self.prodHandler = Ui_Production()
		self.prodHandler.setupUi(self)
		self.setAttribute(Qt.WA_DeleteOnClose)
		
		self.parent = parent
		# parent productions list for modifyProductionWidget uses
		self.productions = self.parent.productions
		self.ui = self.parent.ui
		self.production = production
		self.parent.productions.append(self.production)
		self.setName(self.production.name)
		
	def setName(self, name):
		'''
		Sets the text on the main button with the production name
		'''
		self.prodHandler.productionName.setText( QString(str(self.production.name)) )
		
	def modifyProductionWidget(self, name):
		'''
		Edits the production widget's name
		'''
		self.production.name = name
		self.setName(self.production.name)
		
	'''
	SIGNALS/SLOTS
	'''
	def showProd(self):
		'''
		Shows the production in the workspace
		'''
		self.parent.showProduction(self.production)
	
	def editName(self):
		'''
		Opens a dialog to edit the production object and wrapper object
		'''
		self.productionDialog = prodNameDialogHandler(self)
		self.productionDialog.setName(self.production.name)
		self.productionDialog.show()
		
	def deleteProd(self):
		'''
		Deletes the object and closes the wrapper object
		Also clears the workspace is production is currently in the workspace
		'''
		if self.production == self.parent.currentProduction:
			self.parent.clearWorkspace()
		# show add axiom button if there is at least one production
		if not self.parent.productions:
			self.parent.clearTimeline()
		else:
			# remove all axioms of same name of production
			while self.production in self.parent.axioms:
				index = self.parent.axioms.index(self.production)
				layout = self.parent.ui.timelineLayout
				layout.itemAt(index).widget().close()
				layout.removeItem(layout.itemAt(index))
				self.parent.axioms.remove(self.production)
				self.parent.countAxioms -= 1
			# resets axiom list with updated productions
			self.parent.ui.axiomList.clear()
			for production in self.parent.productions:
				self.parent.ui.axiomList.addItem(QString(production.name))
		self.parent.removeProductionWidget(self)