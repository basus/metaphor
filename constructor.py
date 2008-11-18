class Pattern:
    '''A class that represents a pattern with all relevant information including
    production rules and parameter values'''

    def __init__(self, name, terms, nonterms):
        self.name = name
        self.terms = terms
        self.nonterms = nonterms
        self.productions = []
        self.defer = []
        self.assign = {}
        self.expansions = {}

    def build_productions(self):
        for production in self.productions:
            if not self.expansions.has_key(production[0]):
                self.expansions[production[0]] = {}
            nonterm = self.expansions[production[0]]
            nonterm[production[1]] = production[2]

    def transform(self, token):
        legals = self.expansions[token]
        


class Constructor:
    ''' A class factory that takes the AST from the Parser and the environments
    from the Validator and builds rich Pattern objects'''

    def __init__(self, astree, env_patterns):
        self.astree = astree
        self.env_patterns = env_patterns
        self.patterns = {}

    def create(self):
        for name,value in self.env_patterns():
            new_pattern = Pattern(name,
                                  value[list(set("terms"))],
                                  value[list(set("nonterms"))])
            self.patterns[name] = new_pattern

    def scan_tree(self):
        root = self.astree.root
        toplevels = root.children
        for each_toplevel in toplevels:
            constructs = self.astree.get_children(each_toplevel)
            self.current = self.patterns[constructs[0]]
            if 'is' in constructs:
                parent = each.toplevel.children[1].children[0]
                clone(parent)
            for construct in each_toplevel.children:
                if construct.data == 'Axiom':
                    self.current.axiom == construct.children[0].data
                if construct.data == 'Production':
                    self.production(construct)
                if construct.data == 'Defer':
                    self.current.defer.append(construct.children[0].data)
                if construct.data == 'Assign':
                    param = construct.children[0].data
                    self.current.assign[param] = int(construct.children[0].data)


    def clone(parent):
        tempname = self.current.name
        self.current = copy.deepcopy(self.patterns[parent.data])
        self.current.name = tempname

    def production(self, top):
        pnt = top.children[0]
        plist = top.children[1]
        if pnt.data == 'pnt':
            nonterm = pnt.children[0].data
            param = pnt.children[0].data
        else:
            nonterm = pnt.data
            param = ''
        productions = [x.data for x in plist.children]
        self.current.productions.append(tuple(nonterm, param, productions))

