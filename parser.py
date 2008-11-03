from tree import ASTree
from error import *
import lang

class Parser:

    '''Takes in a text block and creates an Abstract Syntax Tree representing the entire source'''

    def __init__(self, file):
        self.src = file.read()
        self.tokens = self.src.split()
        self.index = 0
        self.srclength = len(self.tokens)
        self.astree = ASTree("program")
        self.keywords = lang.keywords

    def is_name(self, token):
        if token in self.keywords:
            return False
        elif token.isalnum():
            return True
        else:
            return False

    def get_token(self):
        if self.index < self.srclength:
            token = self.tokens[self.index]
            self.index += 1
            return token
        else:
            exit()


    def program(self):
        '''Parses the outer structure of the source code'''
        legals = {"pattern": self.pattern}


        while self.index < self.srclength:
            token = self.get_token()
            if legals.has_key(token):
                self.astree.add(token)
                legals[token]()
            else:
                raise InvalidBlockError(token)

    def pattern(self):
        legals = {"is": self.inherit,
                  "Axiom": self.axiom,
                  "Production": self.production,
                  "Define": self.define,
                  "Defer": self.defer,
                  "Assign": self.assign}

        token = self.get_token()
        if self.is_name(token):
            self.astree.add_static(token)
        token = self.get_token()
        while token != 'end':
            if legals.has_key(token):
                self.astree.add(token)
                legals[token]()
            else:
                raise InvalidPatternRuleError()
            token = self.get_token()
        self.astree.ascend()

    def inherit(self):
        self.astree.add_static(self.get_token())
        self.astree.ascend()

    def axiom(self):
        token = self.get_token()
        if self.is_name(token):
            self.astree.add_static(token)
            self.astree.ascend()
        else:
            raise InvalidNameError(token)

    def production(self):
        token = self.get_token()
        if token.find('[') != -1:
            self.astree.add('pnt')
            self.pnt(token)
            self.astree.ascend()
        else:
            self.astree.add_static(token)
        if self.get_token() == '=>':
            self.astree.add('plist')
            while not token in self.keywords: 
                self.astree.add_static(token)
                token = self.get_token()
            self.astree.ascend()
            self.astree.ascend()
            self.index -= 1
        else:
            raise InvalidProductionError(token)

    def pnt(self, token):
        ls = token.split('[')
        nonterm = ls[0]
        param = ls[1].rstrip(']')
        self.astree.add_static(nonterm)
        self.astree.add_static(param)

    def define(self):
        token = self.get_token()
        self.astree.add_static(token)
        if self.get_token() == '=>':
            self.astree.add('ref')
            self.astree.add_static(self.get_token())
            self.astree.add_static(self.get_token())
            self.astree.ascend()
            self.astree.ascend()
        else:
            print token
            raise InvalidDefinitionError(token)

    def defer(self):
        self.astree.add_static(self.get_token())
        self.astree.ascend()

    def assign(self):
        self.astree.add_static(self.get_token())
        self.astree.add_static(self.get_token())
        self.astree.ascend()


class Valditor:
    ''' Traverses the Abstract Syntax Tree and checks to make sure that all nodes form 
    allowable expressions'''

    def __init__(self, astree):
        self.astree = astree
        self.current = self.astree.root
        self.symbtable = {'patterns':[]}

    def program(self):
        legals = {'patterns': pattern}
        toplevels = self.astree.root.children
        for toplevel in toplevels:
            self.current = toplevel
            legals[toplevel.data]()
        print "Source file validated"

    def pattern(self):
        legals = {"is": self.inherit,
                  "Axiom": self.axiom,
                  "Production": self.production,
                  "Define": self.define,
                  "Defer": self.defer,
                  "Assign": self.assign}
        children = self.current.children
        name = children.pop(0)
        if name in self.symbtable['patterns']:
            raise RepeatedPatternError
        else:
            self.symbtable.['patterns'].append(name)
        for child in children:
            self.current = child
            legals[child]()

    def inherit(self):
        inherit_obj = self.current.children[0]
        parent = inherit_obj.data
        if not parent in self.symbtable['patterns']:
            raise UndefinedPatternError

    def axiom(self):
        axiom = self.current.child[0].data

