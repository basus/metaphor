import os
import imp
import syntax
import semantics
import error
import context

class PyScriptInterface:

    def __init__(self, scriptpath):
        self.stringstack = []
        self.script = imp.load_source('', scriptpath)

    def compile(self):
        grammar = open(self.script.compile)
        parser = syntax.Parser(grammar)
        tree = parser.parse()
        builder = semantics.Builder(tree)
        self.env = semantics.Environment(builder)
        self.grammars = self.env.populate()

    def setcontext(self):
        path = os.getcwd() + '/' + self.script.context
        self.handler = context.ContextHandler(path)
        self.handler.load_context()
        
    def generate(self):
        for command in self.script.generate:
            grammar = command[0]
            num = command[1]
            string = self.env.grammars[grammar].generate(num)
            self.stringstack.append((grammar,string))

    def render(self):
        for output in self.script.render:
            if type(output) == type('str'):
                handler = self.handler
            elif len(output) == 2:
                handler = context.ContextHandler(output[1])
                handler.load_context()
                output = output[0]
                    
            current = self.stringstack.pop()
            ctxstring =  self.env.grammars[current[0]].map(current[1])
            handler.render(ctxstring)
            handler.save(output)
                
    def run(self):
        self.compile()
        self.setcontext()
        self.generate()
        self.render()

                    
