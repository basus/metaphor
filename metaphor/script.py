import os
import imp
import syntax
import semantics
import error
import context

class PyScriptInterface:
    """
    Class implementing the script interface to the Metaphor system. Each method
    corresponds roughly to one function of the system. It allows a Python script
    to be used to control creation of grammars and rendering images in batches.
    See the script format specification for information on how to write a script.
    """

    def __init__(self, scriptpath):
        """
        Loads the actual script as a module so that it can be accessed by the
        rest of the class methods.
        @param string with the path to the script to run
        """
        self.stringstack = []
        self.script = imp.load_source('', scriptpath)

    def compile(self):
        """
        Compiles the grammar file specified in the script and turns it into the
        corresponding grammar objects.
        """
        grammar = open(self.script.compile)
        parser = syntax.Parser(grammar)
        tree = parser.parse()
        builder = semantics.Builder(tree)
        self.env = semantics.Environment(builder)
        self.grammars = self.env.populate()

    def setcontext(self):
        """
        Sets the context to be used for rendering (once again read from the script)
        """
        path = os.getcwd() + '/' + self.script.context
        self.handler = context.ContextHandler(path)
        self.handler.load_context()
        
    def generate(self):
        """
        Generates the strings from the grammars according to the script.
        """
        for command in self.script.generate:
            grammar = command[0]
            num = command[1]
            string = self.env.grammars[grammar].generate(num)
            self.stringstack.append((grammar,string))

    def render(self):
        """
        Renders the images according to the script using the specified context.
        Context can be either the global context specified in the script or a
        separate context specified for that particular string render.
        """
        for output in self.script.render:
            if type(output) == type('str'):
                handler = self.handler
            elif len(output) == 2:
                handler = context.ContextHandler(output[1])
                handler.load_context()
                output = output[0]
                    
            current = self.stringstack.pop(0)
            ctxstring =  self.env.grammars[current[0]].map(current[1])
            handler.render(ctxstring)
            handler.save(output)
                
    def run(self):
        """
        Calls each of the class methods that results in grammars being compiled,
        strings generated and then rendered.
        """
        self.compile()
        self.setcontext()
        self.generate()
        self.render()

                    
