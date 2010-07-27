
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from Ui_AxiomWidget import Ui_Axiom

class axiomHandler(QWidget):
	'''
	Handler for the axiom object
	'''
	def __init__(self, parent, production, position = None):
		'''
		Initializes the axiom object
		'''
		QWidget.__init__(self, parent)
		self.axiomHandler = Ui_Axiom()
		self.axiomHandler.setupUi(self)
		self.setAttribute(Qt.WA_DeleteOnClose)
		
		self.parent = parent
		# parent branch list for modifyAxiomWidget uses
		self.axioms = self.parent.axioms
		self.axiom = production
		if position is None:
			self.parent.axioms.append(self.axiom)
		else:
			self.parent.axioms.insert(position, self.axiom)
		self.setName(self.axiom.name)
		
	def setName(self, name):
		'''
		Sets the text on the main button with the name
		'''
		self.axiomHandler.editButton.setText(str(name))
		
	'''
	SIGNALS/SLOTS
	'''
	def editAxiom(self):
		'''
		Displays a combo box to change the wrapper object
		'''
		index = self.parent.ui.timelineLayout.indexOf(self)
		self.parent.modifyAxiom(index, self)
		
	def deleteAxiom(self):
		'''
		Deletes the closes the wrapper object
		'''
		self.parent.removeAxiomWidget(self)
		
	def moveLeft(self):
		print "left move"
	
	def moveRight(self):
		print "right move"