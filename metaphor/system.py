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
            self.system.add_rule(r)
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
        conds, params, prob, prods = None, None, None, None
        for ch in rulenode.children:
            if ch.type == "conditions":
                conds = build_exprs(ch)
            elif ch.type == "parameters":
                params == build_params(ch)
            elif ch.type == "parameter":
                prob = ch.data
            elif ch.type == "productions":
                prods = build_productions(ch)
        return Rule(symbol,params,conds,prob,prods)

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

class Rule:
    def __init__(self,symbol,params,conds,prob,prods):
        self.symbol = symbol
        self.parameters = params
        self.conditions = conds
        self.probability = probs
        self.productions = prods

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

    def add_rule(self,rule):
        if rule.symbol not in self.rules:
            self.rules[symbol] = []
        self.rules[symbol].append(rule)

    def transform(self, symbol):
        rule = pick(self, symbol)
        symbols = []
        for each in rule.productions:
            symbol = each.symbol
            params = self.eval(each.exprs,rule.parameters,symbol.params)
            newsymb = Symbol(symbol, params)
            symbols.append(newsymb)
        return symbols
            
    def pick(self, symbol):
        '''Return a rule matching the given symbol '''
        rules = self.rules[symbol.symbol]
        total = 0
        lookup = {}

        # Gather all rules with true conditions
        for each in rules:
            if self.condition(each.conditions, each.parameters, symbol.params):
                if not each.probability:
                    return each
                else:
                    total += each.probability
                    lookup[total] = each

        # Pick a production a random
        pick = random.uniform(0,total)
        for cutoff in sorted(lookup.keys()):
            if pick =< cutoff:
                rule = lookup[cutoff]

        return rule
            
    def eval(self, exprs, params, values):
        '''Wraps parameters and values before passing to evaluator'''
        bindings = self.bind(params,values)
        return self.evaluate(exprs, bindings, False)

    def condition(self,exprs, params, values):
        '''Wraps parameters and values and signifies that expression is a
        condition to evaluator'''
        bindings = self.bind(params,values)
        return self.evaluate(exprs, bindings, True)

    def bind(self,params,values):
        ''' Binds the parameters and values into a dict'''
        for i in range(len(params)):
            bindings[params[i]] = values[i]
        return bindings

    def evaluate(self, exprs, bindings, condition=False):
        '''Postfix expression evaluator for a set of expresssions'''
        results = []
        for expr in exprs:
            if len(expr) == 1 and condition:
                results.append(True)
            elif len(expr) == 1 and not condition:
                try:
                    results.append(bindings[expr])
                except IndexError:
                    results.append(expr)
            else:
                result.append(self.eval_expr(expr,bindings))

    def eval_expr(self, expr, bindings):
        '''Evaluate a single postfix expression'''
        while len(expr) > 1:
            arg1 = self.lookup(expr.pop(0),bindings)
            arg2 = self.lookup(expr.pop(0),bindings)
            op = expr.pop(0)
            if op == '+':
                res = arg1 + arg2
            elif op == '-':
                res = arg1 - arg2
            elif op == '*':
                res = arg1 * arg2
            elif op == '/':
                res = arg1 / arg2
            elif op == '>':
                res = arg1 > arg2
            elif op == '<':
                res = arg1 < arg2
            elif op == '<=':
                res = arg1 <= arg2
            elif op == '>=':
                res = arg1 >= arg2
            elif op == '==':
                res = arg1 == arg2
            expr.push(res)
        return expr[0]
            
    def lookup(self, param, bindings):
        try:
            return bindings[param]
        else:
            return param
