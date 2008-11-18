import copy
import random

class Pattern:
    '''A class that represents a pattern with all relevant information including
    production rules and parameter values'''

    def __init__(self, name, terms, nonterms):
        self.name = name
        self.terms = terms
        self.nonterms = nonterms
        self.axiom = ''
        self.productions = []
        self.defer = []
        self.assign = {}
        self.expansions = {}

    def build_productions(self):
        '''Takes the tuple list of productions and converts it into a nested dictionary
        of the form nonterm -> {parameter: productions}'''
        for production in self.productions:
            if not self.expansions.has_key(production[0]):
                self.expansions[production[0]] = {}
            nonterm = self.expansions[production[0]]
            nonterm[production[1]] = production[2]

    def transform(self, token):
        '''Takes in a token and calculates an appropriate replacement string based
        on analyzing the expansions dictionaries'''

        #Get reference to expansion dictionary and initialize probability holder
        followers = self.expansions[token]
        probabilities = {}

        #Check if unparameterized
        if followers.has_key('_'):
               return followers['_']

        #Sum ratios
        total = 0
        for each in followers.iterkeys():
            total += self.assign[each]

        #Generate probabilities
        for each in followers.iterkeys():
            probabilities[each] = self.assign[each]/total
            
        #Invert to get probability -- parameter binding (prob going from 0 to 1)
        point = 0
        lookup = {}
        for param, prob in probabilities.iteritems():
            lookup[point+prob] = param
            point += prob

        #Pick a random number and get expansion corresponding to probability
        pick = random.random()
        cutoffs = lookup.keys()
        cutoffs.sort()
        for cutoff in cutoffs:
            if pick < cutoff:
                return followers[lookup[cutoff]]

    def build_pattern(self, generations):
        axiom = self.axiom
        while generations > 0:
            tempstring = []
            for element in axiom:
                if element in self.nonterms:
                    tempstring.extend(self.transform(element))
                else:
                    tempstring.append(element)
            axiom = tempstring
            generations -= 1
        return axiom
                    


class Constructor:
    ''' A class factory that takes the AST from the Parser and the environments
    from the Validator and builds rich Pattern objects'''

    def __init__(self, astree, env_patterns):
        self.astree = astree
        self.env_patterns = env_patterns
        self.patterns = {}

    def create(self):
        for name,value in self.env_patterns.iteritems():
            new_pattern = Pattern(name,
                                  list(set(value["terms"])),
                                  list(set(value["nonterms"])))
            self.patterns[name] = new_pattern

    def scan_tree(self):
        ''' Traverses the ASTree and builds the Pattern Objects as required'''
        root = self.astree.root
        toplevels = root.children
        for each_toplevel in toplevels:
            constructs = self.astree.get_children(each_toplevel)
            self.current = self.patterns[constructs[0]]
            if 'is' in constructs:

                parent = each_toplevel.children[1].children[0].data
                self.clone(parent)
            for construct in each_toplevel.children:
                if construct.data == 'Axiom':
                    self.current.axiom = construct.children[0].data
                if construct.data == 'Production':
                    self.production(construct)
                if construct.data == 'Defer':
                    self.current.defer.append(construct.children[0].data)
                if construct.data == 'Assign':
                    param = construct.children[0].data
                    self.current.assign[param] = float(construct.children[1].data)
            self.patterns[constructs[0]] = self.current


    def clone(self, parent):
        '''Clones the parent object and sets it as the current object being altered'''
        tempname = self.current.name
        self.current = copy.deepcopy(self.patterns[parent])
        self.current.name = tempname

    def production(self, top):
        
        pnt = top.children[0]
        plist = top.children[1]
        if pnt.data == 'pnt':
            nonterm = pnt.children[0].data
            param = pnt.children[1].data
        else:
            nonterm = pnt.data
            param = '_'
        productions = [x.data for x in plist.children]
        self.current.productions.append(tuple((nonterm, param, productions)))

