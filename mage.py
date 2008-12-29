#!/usr/bin/env python

import sys

import syntax
import semantics
import context
import error


def compile(filename, env=None):
    '''Compiles the given file and adds its Grammars into the current environment '''
    if env == None:
        env = envir
    file = open(filename)
    parser = syntax.Parser(file)
    tree = parser.parse()
    builder = semantics.Builder(tree)
    env.builder = builder
    grammars = env.populate()
    print "Compilation successful. The following grammars are now available:\n"
    for grammar in grammars:
        print grammar
    print '\n'


def generate(grammar):
    pass

def newenv():
    pass

def usecontext(context):
    pass

def init():
    pass

def help(cname=None):
    if cname == None:
        print "The following commands are available: "
    else:
        print fdict[cname].__doc__

def quit():
    sys.exit(0)
    

fdict = { 'compile':compile,
          'generate':generate,
          'newenv':newenv,
          'usecontext':usecontext,
          'quit':quit,
          'help':help,
          }


if __name__ == '__main__':

    envir = semantics.Environment()

    print "Welcome to the Metaphor Interaction Shell"
    print "Type help for a list of instructions"
    instr = ''
    while not instr == 'quit':
        instr = raw_input(">>> ")
        instr = instr.split()
        try:
            fdict[instr[0]](*instr[1:])
        except KeyError:
            print "That command does not exist"
            print "Type help for a list of commands"
        except TypeError:
            print "That command requires additional input"
            print "Type help for additional information"
        except Exception as err:
            print "An error occurred"
            print err
