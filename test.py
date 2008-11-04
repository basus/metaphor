from tree import ASTree
from parser import Parser
from parser import Validator

fl = open('patlang')
parse = Parser(fl)
print "parser made"
parse.program()
print parse.astree.breadth_traverse(parse.astree.root)

valid = Validator(parse.astree)
valid.program()
for key in  valid.env_patterns:
    print key
    print valid.env_patterns[key]
