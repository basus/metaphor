from ply import lex
from ply import yacc
from nodes import Node

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
          "NUMBER", ] + list(reserved.values()) + list(operators.values()) + list(comparators.values())

t_OPEN_PAREN = r"\("
t_CLOSE_PAREN = r"\)"

t_OPEN_BRACE = r"\{"
t_CLOSE_BRACE = r"\}"

t_SEPARATOR = r","

t_ignore_BLANK = r"[ \t\r\f\v]"
t_ignore_comment = r"\#.*"

def t_SPECIAL(t):
    r"(>|<)=?|==|=>|\+|-|\*|/"
    t.type = operators.get(t.value, "SPECIAL")
    if t.type == "SPECIAL":
        t.type = comparators.get(t.value, "SPECIAL")
    return t

def t_SYMBOL(t):
    "[A-za-z]\w*"
    t.type = reserved.get(t.value,"SYMBOL")         # Check is symbol is a keyword
    return t

def t_NUMBER(t):
    r"\d*\.?\d+"
    if t.value.find('.') == -1:
        t.value = int(t.value)
    else:
        t.value = float(t.value)
    return t

def t_error(t):
    raise TypeError("Unknown text %s" % (t.value,))

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

lex.lex()


## Parser section

def p_system(p):
    "system : SYSTEM SYMBOL declarations"
    p[0] = Node("system", p[3], p[2])

def p_declarations(p):
    """
    declarations : declaration declarations
                 | empty
    """
    if len(p) == 3:
        p[0] = Node("declarations", [p[1]])
        p[0].children += p[2].children
    else:
        p[0] = p[1]

def p_declaration(p):
    """
    declaration : axiom
                | define
                | rule
                | render
    """
    p[0] = p[1]

def p_axiom(p):
    """
    axiom : AXIOM SYMBOL
          | AXIOM SYMBOL OPEN_PAREN parameters CLOSE_PAREN
    """
    if len(p) == 3:
        p[0] = Node("axiom", p[2])
    else:
        p[0] = Node("axiom", [p[2], p[4]])


def p_define(p):
    "define : DEFINE SYMBOL PRODUCE NUMBER"
    p[0] = Node("define", [p[2], p[4]])

def p_render(p):
    """
    render : RENDER SYMBOL OPEN_PAREN parameters CLOSE_PAREN PRODUCE productions
           | RENDER SYMBOL PRODUCE productions
    """
    if len(p) == 5:
        p[0] = Node("render", [p[2],p[4]])
    else:
        p[0] = Node("render", [p[2], p[4], p[7]])

def p_rule(p):
    """
    rule : RULE SYMBOL OPEN_PAREN conditions CLOSE_PAREN OPEN_BRACE parameter CLOSE_BRACE PRODUCE productions
         | RULE SYMBOL OPEN_BRACE parameter CLOSE_BRACE PRODUCE productions
         | RULE SYMBOL OPEN_PAREN conditions CLOSE_PAREN PRODUCE productions
    """
    if len(p) == 11:
        p[0] = Node("rule", [p[2],p[4],p[7],p[10]])
    else:
        p[0] = Node("rule", [p[2],p[4],p[7]])

def p_conditions(p):
    """
    conditions : condition SEPARATOR conditions
               | condition
    """
    p[0] = Node("conditions")
    if len(p) == 2:
        p[0].children = [p[1]]
    else:
        p[0].children = [p[1]] + p[3].children

def p_condition(p):
    """
    condition : parameter
              | parameter GT parameter
              | parameter LT parameter
              | parameter EQ parameter
              | parameter GTEQ parameter
              | parameter LTEQ parameter
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node("condition",[p[1],p[3]], p[2])

def p_parameters(p):
    """
    parameters : parameter SEPARATOR parameters
               | parameter
    """
    if len(p) == 2:
        p[0] = Node("parameters", p[1], None)
    else:
        p[0] = Node("parameters", [], None)
        p[0].children = [p[1]] + p[3].children

def p_parameter(p):
    """
    parameter : SYMBOL
              | NUMBER
    """
    p[0] = Node("parameter", None, p[1])

def p_productions(p):
    """
    productions : production productions
                | empty
    """
    if len(p) == 3:
        p[0] = Node("productions")
        p[0].children = [p[1]] + p[2].children
    else:
        p[0] = p[1]

def p_production(p):
    """
    production : SYMBOL
               | SYMBOL OPEN_PAREN expressions CLOSE_PAREN
    """
    if len(p) == 2:
        p[0] = Node("production", [p[1]])
    else:
        p[0] = Node("production", [p[1],p[3]])

def p_expressions(p):
    """
    expressions : expression SEPARATOR expressions
                | expression
    """
    p[0] = Node("expressions")
    if len(p) == 2:
        p[0].children = [p[1]]
    else:
        p[0].children = [p[1]] + p[3].children

def p_expression(p):
    """
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | parameter
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = Node("expression",[p[1],p[3]], p[2])

def p_empty(p):
    """empty : """
    p[0] = Node("empty",[],None)
    pass

def p_error(p):
    if not p:
        print "EOF"
        return p_empty(p)
    else:
        print "Syntax error for ", p.value, " at line ", p.lexer.lineno
    
precedence = (
    ('nonassoc', 'LT', 'GT', 'EQ', 'LTEQ', 'GTEQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

parser = yacc.yacc()
