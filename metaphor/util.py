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
    print root
            
if __name__ == "__main__":
    print_syntax()
    browse_ast()
