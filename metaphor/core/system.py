import random
from parser import parser
from context import ContextHandler
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
        return self.system

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
            r = self.build_rule(decl)
            self.system.add_render(r)
        elif decl.type == "define":
            (symbol, number) = self.build_define(decl)
            self.system.defines[symbol] = number

    def build_axiom(self, axnode):
        axiom = []
        for each in axnode.children:
            symbol = each[0]
            try:
                param = self.build_params(each[1])
            except IndexError:
                param = []
            axiom.append(Symbol(symbol,param))
        return axiom

    def build_rule(self, rulenode):
        symbol = rulenode.children.pop(0)
        conds, params, prob, prods = None, None, None, None
        for ch in rulenode.children:
            if ch.type == "conditions":
                conds = self.build_exprs(ch)
            elif ch.type == "parameters":
                params = self.build_params(ch)
            elif ch.type == "parameter":
                prob = ch.data
            elif ch.type == "productions":
                prods = self.build_productions(ch)
        return Rule(symbol,params,conds,prob,prods)

    def build_define(self, defnode):
        symbol = defnode.children[0]
        number = defnode.children[1]
        return (symbol, number)
    
    def build_render(self, renode):
        if renode.children[1].type == "parameters":
            params = self.build_params(renode.children[1])
            functions = self.build_productions(renode.children[2])
        else:
            params = None
            functions = self.build_productions(renode.children[1])
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
                expressions = self.build_exprs(fn.children[1])
            except IndexError:
                expressions = None
            func = Production(symbol, expressions)
            funcs.append(func)
        return funcs

    def build_exprs(self, exnode):
        exprs = []
        for expr in exnode.children:
            expr = self.build_expr(expr)
            exprs.append(expr)
        return exprs

    def build_expr(self, exnode):
        '''Takes the expression tree from the AST and builds a POSTFIX
        operation string that can be easily evaluated'''
        if exnode.type == "parameter":
            return [exnode.data]
        else:
            stack = []
            stack += self.build_expr(exnode.children[0])
            stack += self.build_expr(exnode.children[1])
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
        self.probability = prob
        self.productions = prods

class System:
    '''A class representing a Lindenmayer System'''

    def __init__(self, name):
        self.name = name
        self.axiom = None
        self.defines = {}
        self.renders = {}
        self.rules = {}

    def add_render(self, render):
        self.renders[render.symbol] = [render]

    def add_rule(self,rule):
        if rule.symbol not in self.rules:
            self.rules[rule.symbol] = []
        self.rules[rule.symbol].append(rule)

    def generate(self, generations):
        '''Generate a compatible string after the given number of generaions'''
        axiom = self.axiom
        while generations > 0:
            temp = []
            for element in axiom:
                if element.symbol in self.rules:
                    new = self.transform(element)
                    temp.extend(new)
                else:
                    temp.append(element)
            axiom = temp
            generations -= 1
        return axiom

    def render(self, generated):
        '''Takes in a generated string and returns a string representing
        context instructions'''
        rules = self.rules
        axiom = self.axiom
        self.rules = self.renders
        self.axiom = generated
        ctx = self.generate(1)
        self.rules = rules
        self.axiom = axiom
        return ctx
        
    def transform(self, symbol):
        rule = self.pick(symbol)
        if not rule: return [symbol]
        symbols = []
        for each in rule.productions:
            symb = each.symbol
            params = self.eval(each.exprs,rule.parameters,symbol.params)
            newsymb = Symbol(symb, params)
            symbols.append(newsymb)
        return symbols
            
    def pick(self, symbol):
        '''Return a rule matching the given symbol '''
        rules = self.rules[symbol.symbol]
        total = 0
        index = {}

        # Gather all rules with true conditions
        for each in rules:
            if self.condition(each.conditions, each.parameters, symbol.params):
                if not each.probability:
                    return each
                else:
                    total += self.lookup(each.probability)
                    index[total] = each

        # Pick a production a random
        pick = random.uniform(0,total)
        for cutoff in sorted(index.keys()):
            if pick <= cutoff:
                return index[cutoff]
            
    def eval(self, exprs, params, values):
        '''Wraps parameters and values before passing to evaluator'''
        if not exprs: return None
        bindings = self.bind(params,values)
        return self.evaluate(exprs, bindings, False)

    def condition(self,conds, params, values):
        '''Wraps parameters and values and signifies that expression is a
        condition to evaluator'''
        if not conds: return True
        bindings = self.bind(params,values)
        return self.evaluate(conds, bindings, True)

    def bind(self,params,values):
        ''' Binds the parameters and values into a dict'''
        if not params: return {}
        bindings = {}
        for i in range(len(params)):
            bindings[params[i]] = values[i]
        return bindings

    def evaluate(self, exprs, bindings, condition=False):
        '''Postfix expression evaluator for a set of expresssions'''
        results = []
        for expr in exprs:
            if len(expr) == 1 and condition:
                if type(expr[0]) == type("str"):
                    results.append(True)
                elif bindings.values()[0] == expr[0]:
                    results.append(True)
                else:
                    results.append(False)
            elif len(expr) == 1 and not condition:
                try:
                    results.append(bindings[expr[0]])
                except:
                    results.append(expr[0])
            else:
                results.append(self.eval_expr(expr,bindings))

        if condition:
            result = True
            for res in results:
                result = result and res
            return res
        else:
            return results

    def eval_expr(self, ex, bindings):
        '''Evaluate a single postfix expression'''
        expr = list(ex)
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
            expr.insert(0,res)
        return expr[0]
            
    def lookup(self, param, bind=None):
        if not bind:
            bindings = self.defines
        else:
            bindings = dict(self.defines)
            bindings.update(bind)
        try:
            return bindings[param]
        except:
            return param

class Environment:
    '''
    Represents the environment in which L-systems are created and their
    strings generated. Provides debug and inspection facilities
    '''

    def __init__(self):
        self.systems = {}
        self.handlers = {}
        self.string_stack = []

    def add(self, sys):
        self.systems[sys.name] = sys

    def add_from_file(self,fname):
        fl = open(fname)
        text = fl.read()
        self.add_from_text(text)

    def add_from_text(self,text):
        systexts = text.split("System ")[1:]
        for systext in systexts:
            systext = "System " + systext
            root = parser.parse(systext)
            builder = Builder(root)
            system = builder.build_system()
            self.systems[system.name] = system

    def add_context(self, handler):
        self.handlers[handler.name] = handler
        self.last_handler = handler.name
        return handler.name

    def add_context_from_file(self, path):
        handler = ContextHandler(path)
        handler.load_context()
        return self.add_context(handler)
        
    def generate(self, name, generations):
        sys = self.systems[name]
        string = sys.generate(generations)
        self.string_stack.append((name,string))
        return string

    def render(self, string=None, handler=None, save=None):
        if not string:
            string = self.string_stack[0]
        if not handler:
            handler = self.last_handler
        sys = self.systems[string[0]]
        ctxstring = sys.render(string[1])
        self.handlers[handler].render(ctxstring)
        self.handlers[handler].save(save)
