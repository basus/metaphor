from tree import ASTree
from parser import Parser

fl = open('patlang')
parse = Parser(fl)
parse.program()
print parse.astree.breadth_traverse(parse.astree.root)
