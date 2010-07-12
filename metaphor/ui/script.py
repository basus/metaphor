import os
import imp

from metaphor.core import context
from metaphor.core import system

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
        path = os.path.abspath(scriptpath)
        self.script = imp.load_source('', path)
        self.gen = self.script.generate
        self.ren = self.script.render
        self.env = system.Environment()

    def compile(self):
        """
        Compiles the grammar file specified in the script and turns it into the
        corresponding grammar objects.
        """
        self.env.add_from_file(self.script.compile)

    def setcontext(self):
        """
        Sets the context to be used for rendering (once again read from the script)
        """
        path = os.path.abspath(self.script.context)
        self.handler = self.env.add_context_from_file(path)
        
    def make(self):
        '''
        Generates the strings and then renders them using the specified context
        '''
        if not len(self.ren) == len(self.gen):
            print "Renders do not match strings"
            
        for i in range(len(self.gen)):
            command = self.gen[i]
            output = self.ren[i]
            
            system = command[0]
            num = command[1]
            string = self.env.generate(system,num)
            
            if type(output) == type('str'):
                handler = self.handler
            elif len(output) == 2:
                path = os.path.abspath(output[1])
                handler = self.env.add_context_from_file(path)
                output = output[0]
            self.env.render(handler=handler,save=output)
                
    def run(self):
        """
        Calls each of the class methods that results in grammars being compiled,
        strings generated and then rendered.
        """
        self.compile()
        self.setcontext()
        self.make()
