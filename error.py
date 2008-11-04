class InvalidBlockError(Exception):
    '''Raised if an invalid top level element is found'''
    def __init__(self, token):
        self.message = "The term %s is not allowed in this part of the file" % token

    def __str__(self):
        return self.message

class InvalidPatternRuleError(Exception):
    '''Raised if an invalid pattern element is found'''
    def __init__(self, token):
        self.message = "The instruction %s is not allowed inside a pattern description " % token

    def __str__(self):
        return self.message

class InvalidNameError(Exception):
    '''Raised if a keyword or pure number is used as a name'''
    def __init__(self, token):
        self.message = " %s is not a valid name. Please check the name formation rules" % token

    def __str__(self):
        return self.message

class InvalidProductionError(Exception):
    '''Raised if a production rule is not well-formed'''
    def __init__(self, token):
        self.message = "Production rule for  %s is not well-formed" % token

    def __str__(self):
        return self.message

class InvalidDefinitionError(Exception):
    '''Raised if a definition is not well formed '''
    def __init__(self, token):
        self.message = " %s is not a valid name. Please check the name formation rules" % token

    def __str__(self):
        return self.message

class UndefinedReferenceError(Exception):
    ''' Raised if a reference used in a Define is not present'''
    def __init__(self, token):
        self.message = " %s is used in a Define statement, but is not present in the file" % token

    def __str__(self):
        return self.message

class UndefinedNameError(Exception):
    '''Raised if a name is used in a Define or Defer without being used in a rule'''
    def __init(self, token):
        self.message = " %s has not been used in any pattern" % token

    def __str__(self):
        return self.message
