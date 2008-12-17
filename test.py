from tree import ASTree
from parser import Parser
from parser import Validator
from constructor import *
from Turtle import Turtle

fl = open('cantor.gr')
parse = Parser(fl)
print "parser made"
parse.program()
parse.astree.breadth_traverse(parse.astree.root)

valid = Validator(parse.astree)
valid.program()

constructor = Constructor(parse.astree, valid.env_patterns)
constructor.create()
constructor.scan_tree()

patterns = constructor.patterns
tree = patterns['CantorDust']
tree.build_productions()

## for nt in tree.productions:
##     print nt

## for nt, exp in tree.expansions.iteritems():
##     print nt, exp
    
## for param, val in tree.assign.iteritems():
##     print param, val
    
#rint tree.transform('trunk')
str =  tree.build_pattern(3)
print str

img = tree.represent(str)
print img

context = Turtle()
for instr in img:
    sep = instr.split('[')
    call = sep[0]
    args = sep[1].rstrip(']')
    args = args.split(',')
    if call == 'move_forward':
        context.move_forward(int(args[0]))
    if call == 'draw_forward':
        context.draw_forward(int(args[0]))
