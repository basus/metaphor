class Node:
    """
    A base class for all other Node classes. Each node represents an type of
    element that can be part of a grammar file. This class provides basic
    accessor methods.
    """

    def __init__(self, data, parent):
        """
        This constructor forms a new node object from the parent of that node
        and the data encapsulated by it.
        @param data: the data element wrapped by the node
        @param parent: the parent of the node in the abstract syntax tree
        """
        self.__parent = parent
        self.__data = data

    def setdata(self, newdata):
        """
        Allows the data element in the node to be replaced. However the type of
        the new data element must match the one being replaced.
        @param newdata : The new data element for the node to wrap. 
        """
        if type(newdata) == type(self.__data):
            self.__data = newdata
        else:
            raise TypeError

    def getdata(self):
        """
        Accessor for the data element that the node wraps.
        """
        return self.__data

    data = property(getdata, setdata)


class RootNode(Node):
    """A class for the roots of the ASTs"""
    def __init__(self):
        """
        The root node requires no parent and this overrides the default
        constructor for Nodes.
        """
        self.parent = None
        self.grammarlist = []

    def add_grammar(self, grammar):
        """
        Only element that can be added directly to a root node is a grammar.
        This method allows a new grammar node to be added to the root.
        """
        self.grammarlist.append(grammar)

class GrammarNode(Node):
    """A class for each individual grammar of the AST"""

    def __init__(self, name, parent):
        """
        Similar to the superclass constructor. The data should be the name of
        the grammar and the parent should be a root node. The grammar's lists
        of productions, mappings and probability assignments are also
        initialized
        @param name : name of the grammar
        @param parent : the parent of this grammar, should be a root node
        """
        self.name = name
        self.parent = parent
        self.productionlist = []
        self.maplist = []
        self.assignlist = []
        self.base = None

    def add_base(self, base):
        """
        Allows a base grammar to be assigned to be assigned to the current
        grammar.
        @param base : the base grammar from which the current one should be
        derived
        """
        self.base = base

    def add_axiom(self, axiom):
        """
        Ands an axiom node for the grammar
        @ param axiom : a string to be used as the start for the generation
        """
        self.axiom = axiom

    def add_production(self, production):
        """
        Allows a production node to be added to the grammar.
        @ param production : a ProductionNode that will be added
        """
        self.productionlist.append(production)

    def add_map(self, map):
        """
        Allows a MapNode to be added to the grammar
        @ param map : a MapNode 
        """
        self.maplist.append(map)

    def add_assign(self, assign):
        """
        Allows an AssignNode to be added to the grammar
        @ param assign : an AssignNode 
        """
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
