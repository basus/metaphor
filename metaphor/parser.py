from ply import lex
from ply import yacc

## Major classes of lexemes

reserved = {
    "System": "SYSTEM",
    "Axiom" : "AXIOM",
    "Rule" : "RULE",
    "Define" : "DEFINE",
    "Render" : "RENDER",
    }

operators = {
    "+" : "PLUS",
    "-" : "MINUS",
    "*" : "TIMES",
    "/" : "DIVIDE",
    "=>" : "PRODUCE"
}

comparators = {
    "<=" : "LTEQ",
    ">=" : "GTEQ",
    "==" : "EQ",
    ">" : "GT",
    "<" : "LT"
    }

tokens = ["SYMBOL", "OPEN_PAREN", "CLOSE_PAREN", "OPEN_BRACE",
          "CLOSE_BRACE", "SPECIAL", "BLANK", "SEPARATOR",
          "INT", "FLOAT", ] + list(reserved.values()) + list(operators.values()) + list(comparators.values())

t_OPEN_PAREN = r"\("
t_CLOSE_PAREN = r"\)"

t_OPEN_BRACE = r"\["
t_CLOSE_BRACE = r"\]"

t_SEPARATOR = r","

t_ignore_BLANK = r"[ \t\r\f\v]"
t_ignore_comment = r"\#.*"

def t_SPECIAL(t):
    r"(>|<)=?|==|=>|,|\+|-|\*|/"
    t.type = operators.get(t.value, "SPECIAL")
    if t.type == "SPECIAL":
        t.type = comparators.get(t.value, "SPECIAL")
    return t

def t_SYMBOL(t):
    "[A-za-z]\w*"
    t.type = reserved.get(t.value,"SYMBOL")         # Check is symbol is a keyword
    return t

def t_INT(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_FLOAT(t):
    r"\d*\.\d+"
    t.value = float(t.value)
    return t

def t_error(t):
    raise TypeError("Unknown test %s" % (t.value,))

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

lex.lex()

f = open("../examples/parametric.gr")
st = ""
for l in f:
    st += l

## Parser section

def p_system(p):
    "system : SYSTEM SYMBOL declarations"
    p[0] = Node("system", p[3], p[2])


def p_declarations(p):
    """declarations : declaration declarations
                  | empty"""
    p[0] = Node("declarations", [p[1]])
    p[0].children += p[2].children

def p_declaration(p):
    """
    declaration : axiom
                | define
                | rule
                | render
    """
    p[0] = p[1]

def p_axiom(p):
    """axiom : AXIOM SYMBOL
           | AXIOM SYMBOL OPEN_PAREN parameters CLOSE_PAREN"""
    if len(p) == 3:
        p[0] = Node("axiom", None, p[2])
    else:
        p[0] = Node("axiom", p[4], p[2])


def p_define(p):
    "define : DEFINE SYMBOL PRODUCE value"
    p[0] = Node("define", None, (p[2],p[4]))

def p_render(p):
    """render : RENDER SYMBOL OPEN_PAREN parameters CLOSE_PAREN PRODUCE functions
              | RENDER SYMBOL PRODUCE functions"""
    pass

def p_rule(p):
    """rule : RULE SYMBOL OPEN_PAREN conditions CLOSE_PAREN OPEN_BRACE parameter CLOSE_BRACE PRODUCE productions
          | RULE SYMBOL OPEN_BRACE parameter CLOSE_BRACE PRODUCE productions
          | RULE SYMBOL OPEN_PAREN conditions CLOSE_PAREN PRODUCE productions"""
    pass

def p_conditions(p):
    """
    conditions : condition SEPARATOR conditions
               | empty
    """
    pass

def p_condition(p):
    """condition : parameter
               | parameter GT parameter
               | parameter LT parameter
               | parameter EQ parameter
               | parameter GTEQ parameter
               | parameter LTEQ parameter
    """
    pass

def p_parameters(p):
    """
    parameters : parameter SEPARATOR parameters
               | parameter
    """
    if len(p) == 2:
        p[0] = Node("parameter", p[1], None)
    else:
        p[0] = Node("parameter", [], None)
        p[0].children = p[1] + p[3].children

def p_parameter(p):
    """
    parameter : SYMBOL
              | value
    """
    if type(p[1]) == Node:
        p[0] = p[1]
    else:
        p[0] = Node("symbol",None,p[1])

def p_productions(p):
    """
    productions : production productions
                | empty
    """
    p[0] = Node("productions", None, None)
    p[0].children += p[1].children

def p_production(p):
    """
    production : SYMBOL
                | SYMBOL OPEN_PAREN expressions CLOSE_PAREN
    """
    if len(p) == 2:
        p[0] = Node("production", None, p[1])
    else:
        p[0] = Node("production", p[3], p[1])

def p_functions(p):
    """
    functions : function functions
              | empty
    """
    p[0] = Node("functions", None, None)
    p[0].children += p[2].children

def p_function(p):
    """
    function : SYMBOL
              | SYMBOL OPEN_PAREN expressions CLOSE_PAREN
    """
    p[0] = Node("function", [])

def p_expressions(p):
    """
    expressions : expression SEPARATOR expressions
                | empty
    """
    pass

def p_expression(p):
    """
    expression : expression PLUS expression
           | expression MINUS expression
           | expression TIMES expression
           | expression DIVIDE expression
           | OPEN_PAREN expression CLOSE_PAREN
           | parameter
    """
    pass

def p_value(p):
    """
    value : INT
           | FLOAT
    """
    p[0] = Node("value", None, p[1])

def p_empty(p):
    "empty :"
    pass

def p_error(p):
    print p.value, p.type
    print yacc.token()
    
precedence = (
    ('nonassoc', 'LT', 'GT', 'EQ', 'LTEQ', 'GTEQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

parser = yacc.yacc()
parser.parse(st)
