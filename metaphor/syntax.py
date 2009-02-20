"""Classes necessary for reading the input in the form of
MeGEN and building abstract syntax trees"""

import nodes
from  error import *

keywords = ['grammar', 'Axiom', 'Production', 'Map', 'is', 'Assign', 'ENDofFILE']


class Parser:
    ''' Recursive Descent Parser for parsing and building the Abstract
    Syntax Tree for a Grammar file '''


    def __init__(self, file):
        self.__file = file

    def parse(self):
        self.fl = self.__file.readlines()
        self.src = []
        for line in self.fl:
            line.rstrip()
            line = line.split()
            self.src.append(line)
        self.src.append(['ENDofFILE'])
        self.lineno = 0
        self.index = 0
        self.treenode = nodes.RootNode()

        self.root()
        return self.treenode

        
    def get_token(self):
        ''' Returns the next token in the file being parsed'''
        try:
            token = self.src[self.lineno][self.index]
            self.index += 1
            return token
        except IndexError:
            self.lineno += 1
            self.index = 0
            return self.get_token()

    def backtrack(self):
        ''' Moves the parser by one token'''
        if self.index > 0:
            self.index -= 1
        else:
            self.lineno -= 1
            self.index = 0

    def root(self):
        ''' Parses the toplevel of the Grammar file and calls the necessary
        Grammar functions. '''
        legals = {'grammar' : self.grammar, 'ENDofFILE': self.end}
        token = self.get_token()
        while self.lineno < len(self.src)-1:
            if token in legals:
                legals[token]()
                token = self.get_token()
            else:
                raise error.InvalidBlockError(token, self.lineno)

    def grammar(self):
        ''' Parses the individual grammars and calls appropriate functions'''
        name = self.get_token()
        grammar = nodes.GrammarNode(name, self.treenode)
        self.treenode.add_grammar(grammar)
        self.treenode = grammar
        
        grammar_legals = {"is": self.inherit,
                          "Axiom": self.axiom,
                          "Production": self.production,
                          "Map": self.map,
                          "Assign": self.assign}


        token = self.get_token()
        while token != 'grammar' and token != 'ENDofFILE':
            if token in grammar_legals.keys():
                grammar_legals[token]()
            else:
                raise InvalidGrammarRuleError(token)
            token = self.get_token()

        self.backtrack()
        self.treenode = grammar.parent

    def inherit(self):
        '''Controls inheritance of grammars'''
        basegrammar = self.get_token()
        self.treenode.add_base(nodes.BaseNode(basegrammar, self.treenode))

    def axiom(self):
        '''Builds nodes for axioms'''
        axiom = []
        token = self.get_token()
        while not token in keywords:
            axiom.append(token)
            token = self.get_token()
        self.treenode.add_axiom(nodes.AxiomNode(axiom, self.treenode))
        self.backtrack()

    def production(self):
        '''Builds the node structure for a production rule'''
        nonterm = self.get_token()
        if nonterm.find('[') != -1:
            ls = nonterm.split('[')
            nonterm = ls[0]
            param = ls[1].rstrip(']')
        else:
            param = '_'
        token = self.get_token()
        if token == '=>':
            productions = []
            token = self.get_token()
            while not token in keywords: 
                productions.append(token)
                token = self.get_token()
        else:
            raise InvalidProductionError(token)
        self.treenode.add_production( nodes.ProductionNode (nonterm, param,
                                                           productions, self.treenode))
        self.backtrack()


    def map(self):
        '''Adds map nodes '''
        element = self.get_token()
        repr = []
        if self.get_token() == '=>':
            token = self.get_token()
            while not token in keywords:
                repr.append(token)
                token = self.get_token()
            self.backtrack()
        else:
            raise error.InvalidGrammarRuleError(token, self.lineno)
        self.treenode.add_map(nodes.MapNode(element, repr, self.treenode))


    def assign(self):
        param = self.get_token()
        value = self.get_token()
        try:
            value = float(value)
        except:
            raise InvalidAssignmentError(value, self.lineno)
        self.treenode.add_assign(nodes.AssignNode(param, value, self.treenode))

    def end(self):
        print "End Reached"
