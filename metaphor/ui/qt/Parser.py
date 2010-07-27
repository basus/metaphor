
from xml.dom import minidom
from grammarPieces import *

class Parser:
	def parseSaveFile(self, xmlFile):
		xmlProductions = []
		grammarNode = minidom.parse(xmlFile).getElementsByTagName("grammar")[0]
		context = str(grammarNode.attributes["context"].value)
		
		for prodNode in grammarNode.getElementsByTagName("entity"):
			prodName = str(prodNode.attributes["name"].value)
			if "axiom" in prodNode.attributes.keys():
				if str(prodNode.attributes["axiom"].value) == "true":
					isAxiom = True
				else:
					isAxiom = False
			newProduction = Production(prodName)
			
			for branchNode in prodNode.getElementsByTagName("subtree"):
				branchName = str(branchNode.attributes["name"].value)
				branchWeight = int(branchNode.attributes["weight"].value)
				newBranch = Branch(branchName, branchWeight)
				
				for actionNode in branchNode.getElementsByTagName("method"):
					actionType = str(actionNode.attributes["name"].value)
					actionValues = str(actionNode.attributes["values"].value).split(",")
					newAction = Action(actionType, actionValues)
					newBranch.actions.append(newAction)
				
				for prod in branchNode.data.split():
					newAction = Action(str(value), ["production"])
					newBranch.actions.append(newAction)
				
				newProduction.branches.append(newBranch)
				
			xmlProductions.append(newProduction)
			
		return xmlProductions