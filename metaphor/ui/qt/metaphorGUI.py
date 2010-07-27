
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import os

import ConfigParser

from grammarPieces				import *
from startWindowHandler			import startWindowHandler
from generateDialogHandler		import generateDialogHandler
from axiomHandler				import axiomHandler
from branchHandler				import branchHandler
from editBranchDialogHandler	import editBranchDialogHandler
from productionHandler			import productionHandler
from prodNameDialogHandler		import prodNameDialogHandler
from Ui_MainWindow				import Ui_MainWindow

class metaphorGUI(QMainWindow):
	'''
	Metaphor's graphical user interface handler
	'''
	def __init__(self):
		'''
		Initializes main window and starting variables
		'''
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.axioms = []
		self.countAxioms = 0
		self.branches = []
		self.countBranches = 0
		self.productions = []
		self.countProductions = 0
		self.currentProduction = None
		
		self.configPath = "./config.txt"
		self.config = ConfigParser.RawConfigParser()
		self.config.read(self.configPath)
		self.currentOpenDir = self.config.get("dirs", "open_dir")
		self.currentSaveDir = self.config.get("dirs", "save_dir")
		self.sampleDir = self.config.get("dirs", "sample_dir")
		self.recentFiles = self.config.get("files", "recent")
		
		self.currentFilename = None
		self.currentContext = None
		
		self.setupWindow()
		self.showStartWindow()
		
	def setupWindow(self):
		'''
		Hides UI components
		'''
		self.ui.addAxiom.hide()
		self.ui.axiomList.hide()
		self.ui.editAxiom.hide()
		self.ui.newBranch.hide()
		
	def showStartWindow(self):
		'''
		Shows the start window
		'''
		contextList = ""
		self.startWindow = startWindowHandler(self, self.recentFiles, self.sampleDir)
		self.startWindow.show()
		
	def softReset(self):
		'''
		Resets the program to a new grammar file of the current context
		'''
		self.clearTimeline()
		self.clearWorkspace()
		self.clearPalette()
		
	def hardReset(self):
		'''
		Resets the program to the start menu
		'''
		self.softReset()
		self.showStartWindow()
		
	def clearTimeline(self):
		'''
		Clears the timeline to its original state
		'''
		# save current axioms array to file (maybe not)
		# move the edit button to the end of the layout
		self.moveEditCombo(-1)
		self.ui.editAxiom.hide()
		# remove all axiom widgets
		layout = self.ui.timelineLayout
		for i in range(self.countAxioms):
			layout.itemAt(i).widget().close()
			layout.removeItem(layout.itemAt(i))
		self.ui.addAxiom.hide()
		self.ui.axiomList.hide()
		# remove all axiom list items
		self.axioms = []
		self.countAxioms = 0
		
	def clearWorkspace(self):
		'''
		Clears the workspace to its original state
		'''
		# save current branches to current production
		if self.currentProduction != None:
			self.currentProduction.branches = self.branches
		layout = self.ui.workspaceLayout
		for i in range(self.countBranches):
			# save each branch's actions
			layout.itemAt(i).widget().saveActions()
			# remove all branch widgets
			layout.itemAt(i).widget().close()
			layout.removeItem(layout.itemAt(i))
		self.ui.newBranch.hide()
		# remove all branch list items
		self.branches = []
		self.countBranches = 0
	
	def clearPalette(self):
		'''
		Clears the palette to its original state
		'''
		# save current productions to file (maybe not)
		# remove all production widgets
		layout = self.ui.paletteLayout
		for i in range(self.countProductions):
			layout.itemAt(i).widget().close()
			layout.removeItem(layout.itemAt(i))
		# remove all production list items
		self.productions = []
		self.countProductions = 0
		
	def modifyBranchWidget(self, name, weight):
		'''
		Creates a branch object and adds it to the layout
		'''
		# create a new branch object
		newBranch = Branch(name, weight)
		# create its handler
		newBranchHandler = branchHandler(self, newBranch)
		# insert the handler into the layout
		self.ui.workspaceLayout.insertWidget(self.countBranches, newBranchHandler)
		# increment the count
		self.countBranches += 1
		print "added branch"
		
	def modifyProductionWidget(self, name):
		'''
		Creates a production object and adds it to the layout
		'''
		# clear the workspace
		self.clearWorkspace()
		# create a new production object
		newProduction = Production(name)
		# set current workspace to new production
		self.currentProduction = newProduction
		# create its handler
		newProductionHandler = productionHandler(self, newProduction)
		# insert the handler into the layout
		self.ui.paletteLayout.insertWidget(self.countProductions, newProductionHandler)
		# increment the count
		self.countProductions += 1
		# now create the first mandatory branch for the production
		# default name: production name
		# default weight: 1
		newBranch = Branch(name, 1)
		newBranchHandler = branchHandler(self, newBranch)
		self.ui.workspaceLayout.insertWidget(self.countBranches, newBranchHandler)
		self.ui.newBranch.show()
		# increment the count
		self.countBranches += 1
		
	def showProduction(self, production):
		'''
		Changes the workspace to show the selected production
		'''
		# clear workspace
		self.clearWorkspace()
		# set current production to this one
		self.currentProduction = production
		# show branches in workspace
		for branch in production.branches:
			newBranchHandler = branchHandler(self, branch)
			# load actions inside the branch
			newBranchHandler.loadActions()
			# add the branch to the layout
			self.ui.workspaceLayout.insertWidget(self.countBranches, newBranchHandler)
			# increment the count
			self.countBranches += 1
		self.ui.newBranch.show()
		# show add axiom button if there is at least one production
		if self.productions:
			if self.ui.axiomList.isHidden():
				self.ui.addAxiom.show()
				self.ui.axiomList.hide()
			else:
				self.ui.addAxiom.hide()
				self.ui.axiomList.clear()
				for production in self.productions:
					self.ui.axiomList.addItem(QString(production.name))
				self.ui.axiomList.show()
		
	def moveEditCombo(self, index):
		'''
		Moves the combo box to given index in timeline layout
		Negative indexes moves it to the end of the layout
		'''
		editCombo = self.ui.editAxiom
		editIndex = self.ui.timelineLayout.indexOf(editCombo)
		editItem = self.ui.timelineLayout.takeAt(editIndex).widget()
		self.ui.timelineLayout.insertWidget(index, editItem)
		
	def modifyAxiom(self, index, axiomHandler):
		self.moveEditCombo(index)
		self.ui.editAxiom.show()
		self.axioms.pop(index)
		axiomHandler.close()
		self.ui.timelineLayout.removeWidget(axiomHandler)
				
	def removeAxiomWidget(self, axiomHandler):
		self.axioms.remove(axiomHandler.axiom)
		self.countAxioms -= 1
		axiomHandler.close()
		self.ui.timelineLayout.removeWidget(axiomHandler)
				
	def removeBranchWidget(self, branchHandler):
		self.branches.remove(branchHandler.branch)
		self.countBranches -= 1
		branchHandler.close()
		self.ui.workspaceLayout.removeWidget(branchHandler)
				
	def removeProductionWidget(self, productionHandler):
		self.productions.remove(productionHandler.production)
		self.countProductions -= 1
		productionHandler.close()
		self.ui.paletteLayout.removeWidget(productionHandler)
		
	def loadFile(self, filepath):
		'''
		Opens a grammar file from given filepath
		'''
		recent = open(self.recentFiles, "r")
		listRecent = recent.readlines()
		recent.close()
		if filepath != "":
			filepath += "\n"
		listRecent.append(filepath)
		setRecent = set(listRecent)
		recent = open(self.recentFiles, "w")
		recent.writelines(setRecent)
		recent.close()
		'''file = open(str(filepath))
		if self.importGrammar(filename):
			self.saveRecentFile(filename)
			self.ui.statusbar.showMessage(Helper.WINDOW_LOAD_STATUS + filename, 0)
			return True
		return False'''
			
	def saveFile(self, filepath):
		'''
		Saves the file under given filename
		'''
		
		'''self.writeGrammar(str(filepath))
		self.ui.statusbar.showMessage(Helper.WINDOW_SAVE_STATUS + str(filepath), 0)'''
		
	def drawImage(self, generations):
		for axiom in self.axioms:
			print "Axiom:", axiom
		for production in self.productions:
			print "Production:", production
			for branch in production.branches:
				print "\tBranch:", branch
				for action in branch.actions:
					print "\t\tAction:", action
		print "run image through metaphor with the grammar at", generations, "generations"
		return True
	
	'''
	SIGNALS/SLOTS
	'''
	
	def newFile(self):
		'''
		Starts a new grammar from current context
		'''
		# call the appropriate new method
		if self.currentContext == "turtle":
			self.newTurtle()
		elif self.currentContext == "BranchContext3D":
			self.newBranch3D()
		elif self.currentContext == "dla3D":
			self.newDla3D()
		else:
			print "cannot make new grammar without context"
			return False
			
	def newTurtle(self):
		'''
		Starts a new grammar with the turtle context
		'''
		self.softReset()
		self.currentFilename = None
		self.currentContext = "turtle"
		print "new turtle grammar"
		return True
	
	def newBranch3D(self):
		'''
		Starts a new grammar with the branch 3D context
		'''
		self.softReset()
		self.currentFilename = None
		self.currentContext = "BranchContext3D"
		print "new branch 3d grammar"
		return True
	
	def newDla3D(self):
		'''
		Starts a new grammar with the dla 3D context
		'''
		self.softReset()
		self.currentFilename = None
		self.currentContext = "dla3D"
		print "new dla 3d grammar"
		return True
	
	def openFile(self):
		'''
		Opens a grammar file
		'''
		filepath = str(QFileDialog.getOpenFileName(self, "Open file...", self.currentOpenDir, "*.xml"))
		self.currentFilename = filepath[filepath.rfind("/")+1:len(filepath)-1]
		self.currentOpenDir = filepath[0:filepath.rfind("/")+1]
		
		return self.loadFile(filepath)
		'''outputFolder = Helper.GRAMMAR_SAVE_FOLDER
		if self.windowTitle() != '' and self.windowTitle() != Helper.MAIN_DEFAULT_WINDOW_NAME:
			outputFolder += str(self.windowTitle())

		if not os.path.exists(outputFolder) or not os.path.isdir(outputFolder):
			ok.mkdir(outputFolder)
		self.grammarFile = QFileDialog.getOpenFileName(self, "Open File", os.getcwd() + '/' + outputFolder, "*.xml")

		if self.grammarFile == None or self.grammarFile == '':
			self.grammarFile = ""
			return False
		return self.openFileFromPath(self.grammarFile)'''
		return True
		
	def clearMenu(self):
		'''
		Clears the list of recently open files
		'''
		print "clear menu"
	
	def saveCurrentFile(self):
		'''
		Saves the currently opened file
		'''
		if self.currentFilename == None:
			return self.saveFileAs()
		else:
			return self.saveFile(self.currentFilename)
		
	def saveFileAs(self):
		'''
		Saves the file under a new name
		'''
		saveDir = self.currentSaveDir
		if self.currentFilename == None:
			saveDir += "untitled."
			saveDir += self.currentContext
			saveDir += ".xml"
		else:
			saveDir += self.currentFilename
		filepath = str(QFileDialog.getSaveFileName(self, "Save file as...", saveDir, "*.xml"))
		self.currentFilename = filepath[filepath.rfind("/")+1:len(filepath)-1]
		self.currentSaveDir = filepath[0:filepath.rfind("/")+1]
		
		return self.saveFile(filepath)
		'''outputFolder = Helper.GRAMMAR_SAVE_FOLDER + self.windowTitle()
		
		if not os.path.exists(outputFolder) or not os.path.isdir(outputFolder):
			os.mkdir(outputFolder)
		
		fileDialog = QFileDialog(self)
		self.grammarFile = fileDialog.getSaveFileName(self, "Save File", os.getcwd() + '/' + outputFolder, "*.xml")
		
		if self.grammarFile == None or self.grammarFile == '':
			return
		elif '.' not in self.grammarFile or self.grammarFile.split('.')[-1] != 'xml':
			self.grammarFile += '.xml'
		
		if fileDialog.confirmOverwrite():
			self.save_file(self.grammarFile)'''
		
	def closeCurrent(self):
		'''
		Closes the current file and resets to the start menu
		'''
		self.hardReset()
	
	def generateImage(self):
		'''
		Opens the generate image dialog
		'''
		self.generateDialog = generateDialogHandler(self)
		self.generateDialog.show()
		
	def help(self):
		'''
		Opens up the help/tutorial window
		'''
		print "help topics"
		
	def about(self):
		'''
		Opens the about window
		'''
		print "about"
			
	def addBranch(self):
		'''
		Opens a dialog to add a branch to the workspace
		'''
		self.branchDialog = editBranchDialogHandler(self)
		self.branchDialog.presetNameOnly(self.currentProduction.name)
		self.branchDialog.show()
		
	def addProduction(self):
		'''
		Opens a dialog to add a production to the workspace
		'''
		self.productionDialog = prodNameDialogHandler(self)
		self.productionDialog.show()
		
	def addAxiom(self):
		'''
		Swaps out the add axiom button for a combo box
		'''
		self.ui.addAxiom.hide()
		self.ui.axiomList.clear()
		self.ui.editAxiom.clear()
		for production in self.productions:
			self.ui.axiomList.addItem(QString(production.name))
			self.ui.editAxiom.addItem(QString(production.name))
		self.ui.axiomList.show()
		
	def selectAxiom(self, index):
		'''
		Selects the production and adds it as an axiom to the layout
		'''
		self.ui.axiomList.hide()
		# grab axiom from the selection
		axiom = self.productions[index]
		# create its handler
		newAxiomHandler = axiomHandler(self, axiom)
		# insert the handler into the layout
		self.ui.timelineLayout.insertWidget(self.countAxioms, newAxiomHandler)
		self.ui.addAxiom.show()
		# increment the count
		self.countAxioms += 1
		
	def insertAxiom(self, index):
		'''
		Inserts axiom at the given index in the layout
		'''
		position = self.ui.timelineLayout.indexOf(self.ui.editAxiom)
		self.moveEditCombo(-1)
		self.ui.editAxiom.hide()
		# grab axiom from the selection
		axiom = self.productions[index]
		# create its handler
		newAxiomHandler = axiomHandler(self, axiom, position)
		# insert the handler into the layout
		self.ui.timelineLayout.insertWidget(position, newAxiomHandler)