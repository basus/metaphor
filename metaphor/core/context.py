import os
import sys
import imp
from error import *
class ContextHandler:
    """
    This class is responsible for handling the interaction between Metaphor and
    context modules. It loads the module from the filename provided and creates
    and object of the Python class in the module. Generated and translated
    strings can be rendered by passing them to the object's render() method.
    Rendered images need to be explicitly saved by calling the save() method with
    the filename.
    """

    def __init__(self, contextpath):
        """
        Sets the path leading to the Python file containing the context code.
        @param contextpath: string defining the path to the context file.
        """
        self.contextpath = contextpath

    def load_context(self):
        """
        Parses the contextpath, loads the Python module and then creates an
        object of the context class.
        """
        try:
            module = imp.load_source('', self.contextpath)
            contextname = self.contextpath.split('/')[-1]
            self.name = contextname.rstrip(".py")
            self.context = getattr(module, self.name)()
        except Exception, e:
            print e
            raise InvalidContextError(self.contextpath)

    def render(self, genstring):
        """
        Steps through the translated string and makes appropriate method calls
        on the context object.

        @param genstring: string representing the instructions to the context
                          object, not the string of grammar symbols
        """
        for action in genstring:
            call = action.symbol
            params = action.params
            try:
                call = getattr(self.context, call)
                if not params:
                    call()
                else:
                    call(*params)
            except AttributeError,a:
                print a
                raise InvalidContextActionError(call)
            except Exception, inst:
                raise ContextAtFaultError(call, inst)

    def save(self, filename):
        """
        Saves the result of context representation with the filename provided.
        Any existing file with the same name will be over-written.

        @param filename: string that is the name of the file that will be
                         created
        """
        try:
            print filename
            self.context.wrapup(filename)
        except Exception, inst:
            print inst
            raise SaveError(inst)


            
