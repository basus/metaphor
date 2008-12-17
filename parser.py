from tree import ASTree
from error import *
from copy import deepcopy
import lang
keywords = lang.keywords

def is_nonterm(token):
    if token.isalnum() and not token in keywords:
        return True
    else:
        return False

def is_term(token):
    rest = token[1:]
    if token[0] == '@' and rest.isalnum() and not rest in keywords:
        return True
    else:
        return False

class Parser:

    '''Takes in a text block and creates an Abstract Syntax Tree representing the entire source'''
    def __init__(self, file):
        self.src = file.read()
        self.tokens = self.src.split()
        self.index = 0
        self.srclength = len(self.tokens)
        self.astree = ASTree("program")
        self.keywords = ["pattern", "Production", "Define", "Defer"]

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
        if is_nonterm(token):
            self.astree.add_static(token)
        token = self.get_token()
        while token != 'end':
            if legals.has_key(token):
                self.astree.add(token)
                legals[token]()
            else:
                raise InvalidPatternRuleError(token)
            token = self.get_token()
        self.astree.ascend()


    def inherit(self):
        self.astree.add_static(self.get_token())
        self.astree.ascend()

    def axiom(self):
        token = self.get_token()
        axiom = []
        while not token in self.keywords:
            axiom.append(token)
            token = self.get_token()
        self.astree.add_static(axiom)
        self.index -= 1
        self.astree.ascend()

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
            token = self.get_token()
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
            self.astree.add_static(self.get_token())
            self.astree.ascend()
        else:
            raise InvalidDefinitionError(token)

    def defer(self):
        self.astree.add_static(self.get_token())
        self.astree.ascend()

    def assign(self):
        self.astree.add_static(self.get_token())
        self.astree.add_static(self.get_token())
        self.astree.ascend()


class Validator:
    ''' Traverses the Abstract Syntax Tree and checks to make sure that all nodes form 
    allowable expressions'''

    def __init__(self, astree):
        self.astree = astree
        self.current = self.astree.root
        self.env_patterns = {}

    def program(self):
        legals = {'pattern': self.pattern}
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
        hold = children.pop(0)
        name = hold.data
        if name in self.env_patterns:
            raise RepeatedPatternError
        else:
            self.env_patterns[name] = {"terms": [],
                                       "nonterms":[],
                                       "productions": [],
                                       "param": [],
                                       "fill":[]}
        self.instance = self.env_patterns[name]
        for child in children:
            self.current = child
            legals[child.data]()

        children.insert(0,hold)

        self.env_patterns[name] = self.instance
        terms = set(self.instance["terms"])
        nonterms = set(self.instance["nonterms"])
        prod = set(self.instance["productions"])
        if len(nonterms.difference(prod)) != 0:
            raise InvalidProductionsError(name)
        


    def inherit(self):
        parent = self.current.children[0].data
        if not parent in self.env_patterns:
            raise UndefinedPatternError(parent)
        else:
            self.instance = deepcopy(self.env_patterns[parent])

    def axiom(self):
        for axiom in self.current.children[0].data:
            if is_nonterm(axiom):
                self.instance["nonterms"].append(axiom)
            else:
                raise InvalidNameError(axiom)

    def production(self):
        lhs = self.current.children[0]
        rhs = self.current.children[1].children
        if lhs.data == 'pnt':
            if is_nonterm(lhs.children[0].data):
                self.instance["nonterms"].append(lhs.children[0].data)
                self.instance["param"].append(lhs.children[1].data)
                self.instance["productions"].append(lhs.children[0].data)
            else:
                raise InvalidNameError(lhs.children[0].data)
        else:
            if is_nonterm(lhs.data):
                self.instance["nonterms"].append(lhs.data)
                self.instance["productions"].append(lhs.data)
            else:
                raise InvalidNameError(lhs.data)
        for element in rhs:
            if is_nonterm(element.data):
                self.instance["nonterms"].append(element.data)
            elif is_term(element.data):
                self.instance["terms"].append(element.data)
            else:
                raise InvalidNameError(element.data)

    def define(self):
        element = self.current.children[0].data
        if not (element in self.instance["nonterms"] or element in self.instance["terms"]):
            raise UndefinedNameError(element)



    def defer(self):
        element = self.current.children[0].data
        if not (element in self.instance["nonterms"] or element in self.instance["terms"]):
            raise UndefinedNameError(element)

    def assign(self):
        param = self.current.children[0].data
        try:
            val = float(self.current.children[1].data)
        except:
            print val, " should be a number"
        if param in self.instance["param"]:
            self.instance["fill"].append((param, val))
        else:
            raise UndefinedNameError(param)
