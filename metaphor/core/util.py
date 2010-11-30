# This file is part of Metaphor.

# Metaphor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Metaphor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Metaphor.  If not, see <http://www.gnu.org/licenses/>.

import re
def syntax():
    "Gathers the token specification and BNF grammars for the parser"
    import parser
    funcs = dir(parser)
    grammars = []
    tokens = []
    
    for fn in funcs:
        if fn.find("p_") == 0:
            grammars.append((fn, getattr(parser,fn).__doc__))
        if fn.find("t_") == 0:
            if type(getattr(parser,fn)) == type('str'):
                tokens.append((fn, getattr(parser,fn)))
            else:
                tokens.append((fn, getattr(parser,fn).__doc__))
    return (tokens,grammars)

def print_syntax():
    '''Print the token specifications and BNF grammars '''
    (tokens, grammars) = syntax()
    print "\n\n===== Printing token regexes =====\n\n"
    for each in tokens:
        print each[0], " --> ", each[1]
    print "\n\n===== Printing BNF Grammar =====\n\n"
    for each in grammars:
        print each[1]

def browse_ast(src=None):
    if not src:
        fl = open("examples/parametric.gr")
        src = ""
        for ln in fl:
            src += ln
            
    import parser
    parser.lex.input(src)
    root = parser.parser.parse(src)
    parent = [root]
    while True:
        comm = input(">> ")

def to2(filein,fileout=None):
    ''' Converts system declaration files to version 3 syntax'''
    fl = open(filein)
    text = fl.read()
    text = text.replace("grammar ", "System ")
    text = text.replace("Production ", "Rule ")
    text = text.replace("Map ", "Render ")
    text = text.replace("[","(")
    text = text.replace("]",")")
    text = re.sub(r'Assign(\s+\w+)(\s+\d*\.?\d+)',r'Define\1 =>\2',text)
    fl.close()
    if fileout:
        fl = open(fileout,'w')
    else:
        fl = open(filein,'w')
    fl.write(text)
    fl.close()
            
if __name__ == "__main__":
    print_syntax()
    browse_ast()
