class ParseError(Exception):
    def __str__(self):
        return "Some parsing error"

class InvalidBlockError(ParseError):
    '''Raised if an invalid top level element is found'''
    def __init__(self, token, line):
        self.message = "!The term %s is not allowed in this part of the file: line %d" % (token, line)

    def __str__(self):
        return self.message

class InvalidGrammarRuleError(ParseError):
    '''Raised if an invalid grammar element is found'''
    def __init__(self, token, line):
        self.message = "The instruction %s is not allowed inside the grammar description" % (token, line)

    def __str__(self):
        return self.message

class InvalidNameError(ParseError):
    '''Currently Unused: Raised if a keyword or pure number is used as a name'''
    def __init__(self, token, line):
        self.message = " %s is not a valid name. Please check the name formation rules" % token

    def __str__(self):
        return self.message

class InvalidProductionError(ParseError):
    '''Raised if a production rule is not well-formed'''
    def __init__(self, token, line):
        self.message = "Production rule for  %s is not well-formed" % token

    def __str__(self):
        return self.message

class InvalidAssignmentError(ParseError):
    '''Raised if a number is not used in an assignment'''
    def __init__(self, token, line):
        self.message = "Error at line %d" % (line, token)

    def __str__(self):
        return self.message

class ContextError(ParseError):
    '''Raised if there is a problem with the Context-based transformation'''

    def __init__(self, action):
        self.message = "The element %s caused an error during the visualization step" % action

    def __str__(self):
        return self.message

class InvalidGrammarError(Exception):
    ''' Raised if an undefined Grammar is asked to generate a string'''

    def __init__(self, gram):
        self.message = "The Grammar %s is not defined" % gram

    def __str__(self):
        return self.message

class InvalidContextError(Exception):
    ''' Raised if an undefined context is used'''

    def __init__(self, gram):
        self.message = "The context %s could not be found" % gram

    def __str__(self):
        return self.message

class NoContextError(Exception):
    ''' Raised if no context is being used'''

    def __init__(self):
        self.message = "There is no context currently defined"

    def __str__(self):
        return self.message
