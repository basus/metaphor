"""
Classes required to implemented the semantics of Metaphor.
Some classes require a proper AST.
"""

class Builder:
    '''Traverses the AST and builds the L-system described'''

    def __init__(self, root=None):
        self.__root = root
        self.node = root

    def build_system(self):
        '''Builds the system starting from the root node'''
        self.system = System(self.__root.data)
        self.build_declarations(self.__root.children)

    def build_declarations(self, declarations):
        decls = declarations.children
        for decl in decls:
            self.build_declaration(decl)

    def build_declaration(self, decl):
        if decl.type == "axiom":
            a = self.build_axiom(decl)
            self.system.axiom = a
        elif decl.type == "rule":
            r = self.build_rule(decl)
            self.system.add_rule(*r)
        elif decl.type == "render":
            r = self.build_render(decl)
            self.system.add_render(*r)
        elif decl.type == "define":
            (symbol, number) = self.build_define(decl)
            self.system.defines[symbol] = number

    def build_axiom(self, axnode):
        symbol = axnode.children[0]
        try:
            param = self.build_params(axnode.children[1])
        except IndexError:
            param = []
        axiom = Symbol(symbol,param)
        return axiom

    def build_rule(self, rulenode):
        symbol = rulenode.children.pop(0)
        conds, params, prods = None, None, None
        for ch in rulenode.children:
            if ch.type == "conditions":
                conds = build_exprs(ch)
            elif ch.type == "parameter":
                prob = ch.data
            elif ch.type == "productions":
                prods = build_prodcutions(ch)
        return (symbol,conds,param,prods)

    def build_define(self, defnode):
        symbol = defnode.children[0]
        number = defnode.children[1]
        return (symbol, number)
    
    def build_render(self, renode):
        if renode.children[1].type == "parameters":
            params = build_params(renode.children[1])
            functions = build_productions(renode.children[2])
        else:
            params = None
            functions = build_productions(renode.children[1])
        symbol = Symbol(renode.children[0], params)
        return (symbol, functions)

    def build_params(self, params):
        paramlist = []
        for param in params.children:
            paramlist.append(param.data)
        return paramlist

    def build_productions(self, fns):
        funcs = []
        for fn in fns.children:
            symbol = fn.children[0]
            try:
                expressions = build_exprs(fn.children[1])
            except IndexError:
                expressions = None
            func = Production(symbol, expressions)
            funcs.append(func)
        return funcs

    def build_exprs(self, exnode):
        exprs = []
        for expr in exnode.children:
            expr = build_expr(expr)
            exprs.append(expr)
        return exprs

    def build_expr(self, exnode):
        '''Takes the expression tree from the AST and builds a POSTFIX
        operation string that can be easily evaluated'''
        if exnode.type == "parameter":
            return [exnode.data]
        else:
            stack = []
            stack += build_expr(exnode.children[0])
            stack += build_expr(exnode.children[1])
            stack.append(exnode.data)
            return stack
            

class Symbol:
    def __init__(self,symbol,params=None):
        self.symbol = symbol
        self.params = params

class Production:
    def __init__(self,symbol,exprs=None):
        self.symbol = symbol
        self.exprs = exprs

class System:
    '''A class representing a Lindenmayer System'''

    def __init__(self, name):
        self.name = name
        self.axiom = None
        self.defines = {}
        self.renders = {}
        self.rules = {}

    def add_render(self, symbol, functions):
        self.renders{symbol.symbol} = (symbol.params, functions)

    def add_rule(self,symbol,conds,prob,prods):
        if symbol not in self.rules:
            self.rules[symbol] = []
        self.rules[symbol].append((conds, prob, prods))

    def transform(self, symbol):
        production = pick(self, symbol)
        symbols = []
        for each in production:
            symbol = each.symbol
            params = evaluate(each.exprs,symbol.params)
            newsymb = Symbol(symbol, params)
            symbols.append(newsymb)
        return symbols
            
    def pick(self, symbol):
        transforms = self.rules[symbol.symbol]
        total = 0
        lookup = {}

        # Gather all rules with true conditions
        for each in transforms:
            if evaluate(each[0], symbol.params):
                if not each[1]:
                    return each[2]
                else:
                    total += each[1]
                    lookup[total] = each[2]

        # Pick a production a random
        pick = random.uniform(0,total)
        for cutoff in sorted(lookup.keys()):
            if pick =< cutoff:
                production = lookup[cutoff]

        return production
            
    def evaluate(self, exprs, params):
        '''Postfix expression evaluator'''
