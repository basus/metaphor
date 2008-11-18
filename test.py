from tree import ASTree
from parser import Parser
from parser import Validator
from constructor import *

fl = open('patlang')
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
tree = patterns['Oak']
tree.build_productions()

## for nt in tree.productions:
##     print nt

## for nt, exp in tree.expansions.iteritems():
##     print nt, exp
    
## for param, val in tree.assign.iteritems():
##     print param, val
    
#rint tree.transform('trunk')
print tree.build_pattern(5)

