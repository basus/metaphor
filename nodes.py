class Node:
    '''A base class for all other Node classes'''

    def __init__(self, data, parent):
        self.__parent = parent
        self.__data = data

    def setdata(self, newdata):
        if type(newdata) == type(self.__data):
            self.__data = newdata
        else:
            raise TypeError

    def getdata(self):
        return self.__data

    data = property(getdata, setdata)


class RootNode(Node):
    '''A class for the roots of the ASTs'''
    def __init__(self):
        self.parent = None
        self.grammarlist = []

    def add_grammar(self, grammar):
        self.grammarlist.append(grammar)

class GrammarNode(Node):
    '''A class for each individual grammar of the AST'''

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.productionlist = []
        self.maplist = []
        self.assignlist = []
        self.base = None

    def add_base(self, base):
        self.base = base

    def add_axiom(self, axiom):
        '''Ands an axiom for the grammar'''
        self.axiom = axiom

    def add_production(self, production):
        self.productionlist.append(production)

    def add_map(self, map):
        self.maplist.append(map)

    def add_assign(self, assign):
        self.assignlist.append(assign)

class AxiomNode(Node):
    '''A class for the axiom of a Grammar'''
    def __init__(self, axiom, parent):
        Node.__init__(self, axiom, parent)
        self.axiom = self.data

class BaseNode(Node):
    ''' A class for the (optional) base node for a Grammar'''
    def __init__(self, axiom, parent):
        Node.__init__(self, axiom, parent)
        self.base = self.data

class MapNode(Node):
    '''A class for the containing a mapping from a Grammar element to a
    context representation.'''

    def __init__(self, elem, repr, parent):
        self.element = elem
        self.repr = repr
        self.__parent = parent

class AssignNode(Node):
    ''' A class for containing the assignment of a numberic value to a parameter'''

    def __init__(self, param, value, parent):
        self.param = param
        self.value = value
        self.__parent = parent

class ProductionNode(Node):
    ''' A class representing non-terminals, parameters and their productions'''

    def __init__(self, nonterm, param, productions, parent):
        self.nonterm = nonterm
        self.param = param
        self.productions = productions
        self.__parent = parent
