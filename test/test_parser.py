from metaphor import parser as p
import os

def lex(text, types, values):
    p.lex.input(text)

    for i in range(len(types)):
        t = p.lex.token()
        print "Lexer found: ", t.type, t.value
        print "Test expected: ", types[i], values[i]
        assert t.type == types[i]
        assert t.value == values[i]
    
def test_all():
    fl = open("examples/parametric.gr")
    st = ""
    for line in fl:
        st += line
    p.lex.input(st)
    p.parser.parse(st)
    pass

def test_RESERVED():
    text = "System Axiom Rule Define Render"
    types = ["SYSTEM", "AXIOM", "RULE", "DEFINE", "RENDER"]
    values = text.split()
    lex(text, types, values)

def test_NUMBER():
    text = "1 1.1 0 0.2 .3 7.4"
    types = ["NUMBER"]*6
    values = [1, 1.1, 0, 0.2, .3, 7.4]
    lex(text, types, values)

def test_OPERATORS():
    text = "+ - * / =>"
    types = ["PLUS", "MINUS", "TIMES", "DIVIDE", "PRODUCE"]
    values = text.split()
    lex(text, types, values)

def test_COMPARATORS():
    text = "<= >= == > <"
    types = ["LTEQ", "GTEQ", "EQ", "GT", "LT"]
    values = text.split()
    lex(text, types, values)

def test_PARENS():
    text = "(a)"
    types = ["OPEN_PAREN", "SYMBOL", "CLOSE_PAREN"]
    values = ["(", "a", ")"]
    lex(text,types,values)

def test_BRACES():
    text = "{x}"
    types = ["OPEN_BRACE", "SYMBOL", "CLOSE_BRACE"]
    values = ["{", "x", "}"]
    lex(text, types, values)
    
def test_SEPARATOR():
    text = "3, x, 5.5, Define"
    types = ["NUMBER", "SEPARATOR", "SYMBOL", "SEPARATOR",
             "NUMBER", "SEPARATOR", "DEFINE"]
    values = [3, ",", "x", ",", 5.5, ",", "Define"]
    lex(text, types, values)
