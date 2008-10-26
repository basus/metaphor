from tree import ASTree

class Parser:

    '''Takes in a text block and creates an Abstract Syntax Tree representing the entire source'''

    def __init__(self, file):
        self.src = file.read()
        self.tokens = self.src.split()
        self.index = 0
        self.srclength = len(self.tokens)
        self.keywords = ['pattern', 'Axiom', 'Production', 'Define', 'Defer', 'is']
        self.astree = ASTree("program")

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
                raise InvalidBlockError()

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