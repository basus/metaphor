class Pattern:
    '''A class that represents a pattern with all relevant information including
    production rules and parameter values'''

    def __init__(self, name, terms, nonterms):
        self.name = name
        self.terms = terms
        self.nonterms = nonterms

class Constructor:
    ''' A class factory that takes the AST from the Parser and the environments
    from the Validator and builds rich Pattern objects'''

    def __init__(self, astree, env_patterns):
        self.astree = astree
        self.env_patterns = env_patterns
        self.pattern_list = []

    def create(self):
        for name,value in self.env_patterns():
            new_pattern = Pattern(name,
                                  value[list(set("terms"))],
                                  value[list(set("nonterms"))])
            self.pattern_list.append(new_pattern)

    def 