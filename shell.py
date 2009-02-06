#!/usr/bin/env python
import sys

import syntax
import semantics
import context
import error

class Shell(object):

    def __init__(self, env=semantics.Environment()):
        self.__env = env
        self.stringstack = []
        self.stringdict = {}

    
    def compile(self, filename):
        '''Compiles the given file and adds its Grammars into the current environment '''
        file = open(filename)
        parser = syntax.Parser(file)
        tree = parser.parse()
        builder = semantics.Builder(tree)
        self.__env.builder = builder
        grammars = self.__env.populate()
        print "Compilation successful. The following grammars are now available:\n"
        for grammar in grammars:
            print grammar
        print '\n'

    def generate(self, grammar, generations=2):
        '''Generates the given grammar name with the number of generations and saves the string '''
        try:
            generations = int(generations)
            string = self.__env.grammars[grammar].generate(generations)
            self.stringstack.append((grammar,string))
            print string
            return string
        except KeyError:
            raise error.InvalidGrammarError(grammar)

    def usecontext(self, ctx):
        '''Sets the specified context as the one to use. '''
        handler = context.ContextHandler(ctx)
        path = sys.path[0] + '/contexts'
        sys.path.insert(0, path)
        self.context = handler.get_context()
        sys.path.pop(0)

    def generateas(self, grammar, generations, name):
        self.stringdict[name] = self.generate(grammar, generations)

    def interpretlast(self, filename):
        '''Interprets the last created string in the current context '''
        try:
            gram, str = self.stringstack[-1]
            ctxstring = self.__env.grammars[gram].map(str)
            self.context.create(ctxstring)
            self.context.save(filename)
            print "The file %s has been created\n" % filename            
        except AttributeError:
            raise error.NoContextError
        
    def help(self, cname=None):
        if cname == None:
            print "The following commands are available: "
        else:
            print getattr(self, cname).__doc__

    def quit(self):
        sys.exit(0)



if __name__ == '__main__':

    shell = Shell()

    print "Welcome to the Metaphor Interaction Shell"
    print "Type help for a list of instructions"

    instr = ''
    while not instr == 'quit':
        instr = raw_input(">>> ")
        instr = instr.split()
        try:
            comm = getattr(shell, instr[0])
            comm(*instr[1:])
        except AttributeError:
            print "That command does not exist"
            print "Type help for a list of commands"
        except TypeError:
            print "That command requires additional input"
            print "Type help for additional information"
        except Exception, err:
            print "An error occurred: \n"
            print err

            

        
