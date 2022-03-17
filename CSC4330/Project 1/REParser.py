import ply.yacc as yacc
from RELexer import tokens
from RENode import RENode

def p_Begin(p):
    "start : re SEMI"
    n = RENode()
    n._operator = '.'
    n._lchild = p[1]
    hasht = RENode()
    hasht._operator = 'leaf'
    hasht._symbol = '#'
    n._rchild = hasht
    p[0] = n
    #p[0] = p[1]

def p_re1(p):
    "re : term"
    p[0] = p[1]

def p_rePLUS(p):
    "re : re PLUS term"
    n = RENode()
    n._operator = '+'
    n._lchild = p[1]
    n._rchild = p[3]
    p[0] = n
    
def p_term(p):
    "term : factor"
    p[0] = p[1]

def p_term1(p):
    "term : term factor"
    n = RENode()
    n._operator = '.'
    n._lchild = p[1]
    n._rchild = p[2]
    p[0] = n

def p_factor(p):
    "factor : exp"
    p[0] = p[1]

def p_factor2(p):
    "factor : factor STAR"
    n = RENode()
    n._operator = '*'
    n._lchild = p[1]
    p[0] = n

def p_var(p):
    "exp : LETTER"
    n = RENode()
    n._operator = 'leaf'
    n._symbol = p[1]
    p[0] = n

def p_var2(p):
    "exp : EPSILON"
    n = RENode()
    n._operator = 'leaf'
    n._symbol = '^'
    p[0] = n

def p_var3(p):
    "exp : LBRAC re RBRAC"
    p[0] = p[2]

parser = yacc.yacc()
