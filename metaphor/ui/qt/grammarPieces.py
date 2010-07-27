
		
class Action:
	'''
	Action object
	'''
	def __init__(self, type, values):
		self.type = type
		self.values = values
		
class Branch:
	'''
	Branch object
		Stores actions
	'''
	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
		self.actions = []
		
class Production:
	'''
	Production object
		Stores branches
	'''
	def __init__(self, name):
		self.name = name
		self.branches = []