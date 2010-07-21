import random
import error
import parser
from context import ContextHandler
"""
Classes required to implemented the semantics of Metaphor.
Some classes require a proper AST.
"""

class Builder:
    """
    Traverses the AST and builds the L-system described
    """

    def __init__(self, root=None):
        """
        Initiate the builder object
        @param root The root node of the AST
        """
        self.root = root
        self.node = root

    def build_system(self):
        """
        Builds the system starting from the root node
        """
        self.system = System(self.root.data)
        self.build_declarations(self.root.children)
        return self.system

    def build_declarations(self, declarations):
        """
        Build all the declarations
        @param the root of the declarations tree
        """
        decls = declarations.children
        for decl in decls:
            self.build_declaration(decl)

    def build_declaration(self, decl):
        """
        Traverse each declaration tree and add the required properties to the
        system object being created
        @param decl The root node of the declaration
        """
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
        """
        Traverses the parse tree for an axiom and returns a Symbol object for it
        @param axnode: The root of the axiom parse tree
        @rtype: Symbol
        @return: A symbol representing the axiom for the Lsystem
        """
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
        """
        Traverses the parse tree for a rule and creates a rule object
        @param rulenode: the root node for the rule's parse tree
        @rtype: Rule
        @return: A Rule object representing the rule in the parse tree
        """
        symbol = rulenode.children.pop(0)
        conds, params, prob, prods = None, None, None, None

        # Based on the type of the AST perform a different action
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
        """
        Return a tuple of the symbol and its defined value from
        @param defnode: The define node
        @rtype: tuple
        @return: Tuple of the symbol and its value
        """
        symbol = defnode.children[0]
        number = defnode.children[1]
        return (symbol, number)
    
    def build_render(self, renode):
        """
        Traverse a render node and return the symbol and the functions it renders as
        @param renode: The root node of the render parse tree
        @rtype: tuple (Symbol, list of functions)
        @return: A tuple of the Symbol and its mapped-to functions
        """
        if renode.children[1].type == "parameters":
            params = self.build_params(renode.children[1])
            functions = self.build_productions(renode.children[2])
        else:
            params = None
            functions = self.build_productions(renode.children[1])
        symbol = Symbol(renode.children[0], params)
        return (symbol, functions)

    def build_params(self, params):
        """
        Create the list of parameters
        @param params: The param parse node
        @rtype: list
        @return: a list of values or symbols representing the parameters
        """
        paramlist = []
        for param in params.children:
            paramlist.append(param.data)
        return paramlist

    def build_productions(self, fns):
        """
        Builds the list of productions including symbols and expressions
        @param fns: the node representing the list of functions
        @rtype: list of Production objects
        @return: the list of Production objects for a Symbol
        """
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
        """
        Build the list of expressions
        @param exnode: the node for the list of expressions
        @rtype: list of expressions
        @return A list of expressions
        """
        exprs = []
        for expr in exnode.children:
            expr = self.build_expr(expr)
            exprs.append(expr)
        return exprs

    def build_expr(self, exnode):
        """
        Takes the expression tree from the AST and builds a POSTFIX
        operation string recursively for later evaluation
        @param exnode: The root node for the expression tree
        @rtype: list
        @return: the expression in postfix form
        """
        if exnode.type == "parameter":
            return [exnode.data]
        else:
            stack = []
            stack += self.build_expr(exnode.children[0])
            stack += self.build_expr(exnode.children[1])
            stack.append(exnode.data)
            return stack
            

class Symbol:
    """Class representing a symbol: the actual symbol and a list of parameters"""
    def __init__(self,symbol,params=None):
        self.symbol = symbol
        self.params = params

class Production:
    """Class representing a single production -- a symbol and a list of expression"""
    def __init__(self,symbol,exprs=None):
        self.symbol = symbol
        self.exprs = exprs

class Rule:
    """Class representing a rule -- the symbol, it's parameters, conditions,
    probability and the list of productions
    """
    def __init__(self,symbol,params,conds,prob,prods):
        self.symbol = symbol
        self.parameters = params
        self.conditions = conds
        self.probability = prob
        self.productions = prods

class System:
    """A class representing a Lindenmayer System"""

    def __init__(self, name):
        """ Initialize the System. Add the name and create the blank dicts
        @type name: string
        @param name: the name of the L-system
        """
        self.name = name
        self.axiom = None
        self.defines = {}
        self.renders = {}
        self.rules = {}

    def add_render(self, render):
        """ Add the render object to the dictionary """
        self.renders[render.symbol] = [render]

    def add_rule(self,rule):
        """
        Add the rule to the list of rules for each symbol. If it is a new
        symbol create a blank list first
        @type rule: Rule
        @param rule: the rule to be added
        """
        if rule.symbol not in self.rules:
            self.rules[rule.symbol] = []
        self.rules[rule.symbol].append(rule)

    def generate(self, generations):
        """Generate a compatible string after the given number of generaions
        @type generations: integer
        @param generations: the number of generations to iterate for
        @rtype: list of Symbol objects
        @return: the generated list of symbols after the given generations
        """
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
        """Takes in a generated string and returns a string representing
        context instructions. Uses the generate() mechanism but replaces the
        rules dictionaries with the renders dictionary and iterates for a
        single generation
        
        @type generated: list of symbols
        @param generated: the list of generated symbols to be rendered
        """
        rules = self.rules
        axiom = self.axiom
        self.rules = self.renders
        self.axiom = generated
        ctx = self.generate(1)
        self.rules = rules
        self.axiom = axiom
        return ctx
        
    def transform(self, symbol):
        """Take in a symbol and return a list of symbols according to the
        production rules. Evaluates the expressions using the parameters of the
        given symbol
        
        @type symbol: Symbol object
        @param symbol: the object whose productions to return
        @rtype: list of symbols
        @return: the list of symbols
        """
        rule = self.pick(symbol)
        if not rule: return [symbol]
        symbols = []
        for each in rule.productions:
            symb = each.symbol
            params = self.eval(each.exprs,rule.parameters,symbol.params)
            newsymb = Symbol(symb, params)
\            symbols.append(newsymb)
        return symbols
            
    def pick(self, symbol):
        """ Return a rule matching the given symbol
        @type symbol: symbol object
        @param symbol: the symbol whose rule to return
        @rtype: Rule object, or None
        @return: A Rule object for the symbol or None
        """
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
        """ Wraps parameters and values before passing to evaluator. Or if there
        is no expression return None.
        """
        if not exprs: return None
        bindings = self.bind(params,values)
        return self.evaluate(exprs, bindings, False)

    def condition(self,conds, params, values):
        """ Wraps parameters and values and signifies that expression is a
        condition to evaluator. If there is no condition, return True
        """
        if not conds: return True
        bindings = self.bind(params,values)
        return self.evaluate(conds, bindings, True)

    def bind(self,params,values):
        """ Binds the parameters and values into a dict
        @type param: list
        @param params: the list of parameters
        @type values: list
        @param values: the list of values for the corresponding parameters
        @rtype: dict
        @return: dictionary mapping parameters to their values
        """
        if not params: return {}
        bindings = {}
        for i in range(len(params)):
            bindings[params[i]] = values[i]
        return bindings

    def evaluate(self, exprs, bindings, condition=False):
        """ Postfix expression evaluator for a set of expresssions
        @type exprs: list
        @param exprs: list of expressions to evaluate
        @type bindings: dict
        @param bindings: the mapping from parameters to values
        @rtype: list
        @return: the list of expression evaluation results"""
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

        # AND over all the conditions to see if the combination is true
        if condition:
            result = True
            for res in results:
                result = result and res
            return res
        else:
            return results

    def eval_expr(self, ex, bindings):
        """Evaluate a single postfix expression"""
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
        """
        Perform a name lookup, with priority given to local bindings and then
        to global defines
        """
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
    """Replaces the environment in which L-systems are created and their
    strings generated. Provides debug and inspection facilities
    """

    def __init__(self):
        """ Initialize the system by making blank dicts for the Lsystems and
        context handlers. Also create a blank stack.
        """
        self.systems = {}
        self.handlers = {}
        self.string_stack = []

    def add(self, sys):
        """ Add an Lsystem to the environment
        @type sys: System object
        @param sys: The Lsystem to be added
        """
        self.systems[sys.name] = sys

    def add_from_file(self,fname):
        """ Add Lsystems from a given file path
        @type fname: string
        @param fname: path to the file to containing Lsystem declarations
        """
        fl = open(fname)
        text = fl.read()
        self.add_from_text(text)

    def add_from_text(self,text):
        """ Add Lsystems from a given block of text
        @type text: string
        @param text: the string with Lsystem declarations
        """
        systexts = text.split("System ")[1:]
        for systext in systexts:
            systext = "System " + systext
            root = parser.parser.parse(systext)
            if parser.err:
                raise error.ParseError(parser.sys['name'], parser.err)
            else:
                builder = Builder(root)
                system = builder.build_system()
                self.systems[system.name] = system

    def add_context(self, handler):
        """ Add a context object the Environment
        @type handler: ContextHandler
        @param handler: the context handler to add to the environment
        """
        self.handlers[handler.name] = handler
        self.last_handler = handler.name
        return handler.name

    def add_context_from_file(self, path):
        """ Add a context from a file to the environment
        @type path: string
        @param path: The path to a .py file meeting the context specifications
        """
        handler = ContextHandler(path)
        handler.load_context()
        return self.add_context(handler)
        
    def generate(self, name, generations):
        """ Generate a string of the given Lsystem for the given number of
        generations
        @type name: string
        @param name: the name of the Lsystem to generate
        @type generations: integer
        @param generations: the number of generations to iterate for
        """
        sys = self.systems[name]
        string = sys.generate(generations)
        self.string_stack.append((name,string))
        return string

    def render(self, string=None, handler=None, save=None):
        """ Render a string in a given context and save the output to a file
        @type string: list of Symbols
        @param string: The string to render, None for one on top of stack
        @type handler: string
        @param handler: the name of the context to use for rendering
        @type save: string
        @param save: the path to the output file
        """
        if not string:
            string = self.string_stack[0]
        if not handler:
            handler = self.last_handler
        sys = self.systems[string[0]]
        ctxstring = sys.render(string[1])
        self.handlers[handler].render(ctxstring)
        self.handlers[handler].save(save)
