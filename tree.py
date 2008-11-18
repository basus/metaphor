from copy import deepcopy
class ASTree:
    '''A generic tree class that can be used to implement an abstract syntax tree'''

    class Node:
        ''' Internal class to represent nodes of the tree'''

        def __init__(self, parent, data, children):
            self.parent = parent
            self.data = data
            self.children = children


    def __init__(self, root):
        '''Creates a new tree with a root and sets current pointer to the root'''
        self.root = self.Node(None, root, [])
        self.now = self.root

    def add_child(self, parent, data):
        '''Adds a child node to a given parent and returns a reference to the new node'''
        child = self.Node(parent, data, [])
        parent.children.append(child)
        return child


    def get_children(self, node):
        ''' Returns a list of references to all children of a node'''
        childlist = [] 
        for child in node.children:
            childlist.append(child.data)
        return childlist

    def add(self, data):
        '''Adds a child to the current node and then moves to the child'''
        self.now = self.add_child(self.now, data)

    def add_static(self, data):
        '''Adds a child to the current node but does not move'''
        self.add_child(self.now, data)

    def ascend(self):
        '''Moves to the parent of the current node'''
        self.now = self.now.parent

    def breadth_traverse(self, start):
        '''Performs a breadth-first traversal of the tree starting from a node'''
        current = start
        children = deepcopy(current.children)
        elements = [current.data]
        for child in children:
            elements.append(child.data)
            for subchild in child.children:
                children.append(subchild)
        self.breadth = elements

class Pattern:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
