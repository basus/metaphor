class ParseError(Exception):
    def __init__(self, system, errors):
        self.system = system
        self.errors = errors
        
    def __str__(self):
        msg = "The following errors were found: \n"
        errs = '\n'.join(["Unexpected Token " + `err[0]` + " at line " +
                          `err[1]` + " in system " +
                          self.system for err in self.errors])
        return msg + errs

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

###############################################
#  End of parse errors
#
###############################################
    
class ContextError(Exception):
    '''Raised if there is a problem with the Context-based transformation'''

    def __init__(self, action):
        self.message = "The element %s caused an error during the visualization step" % action

    def __str__(self):
        return self.message

class InvalidContextError(ContextError):
    ''' Raised if an undefined context is used'''

    def __init__(self, gram):
        self.message = " %s is not a valid context." % gram

    def __str__(self):
        return self.message

class NoContextError(ContextError):
    ''' Raised if no context is being used'''

    def __init__(self):
        self.message = "There is no context currently defined"

    def __str__(self):
        return self.message

class InvalidContextActionError(ContextError):
    '''Raised if a context does not have a specified action '''

    def __init__(self, call):
        self.message = "The action %s is not allowed by the context in use" % call

    def __str__(self):
        return self.message

class ContextAtFaultError(ContextError):
    '''Raised if a context method caused an error. '''

    def __init__(self, call, inst):
        self.message = "The context did not perform the action %s. Error raised is %s" % (call, inst)

    def __str__(self):
        return self.message

class SaveError(ContextError):
    ''' Raised if the result of the rendering could not be saved'''

    def __init__(self, inst):
        self.message = "The following occurred when the result was being saved: %s" %inst


#############################################
# Context Errors End
#
############################################
class InvalidGrammarError(Exception):
    ''' Raised if an undefined Grammar is asked to generate a string'''

    def __init__(self, gram):
        self.message = "The Grammar %s is not defined" % gram

    def __str__(self):
        return self.message
