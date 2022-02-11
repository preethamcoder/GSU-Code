import ply.yacc as yacc
from WFFLexer import tokens


precedence = (
    ('left', 'AND', 'OR'),
    ('left', 'NOT'),
)

def p_Begin(p):
    'BEGIN : START SEMI'
    p[0] = p[1]

def p_Start(p):
    'START : WFF'
    p[0] = ['WFF', p[1]]

def p_WFF_PAR(p):
    'WFF : LBRAC WFF RBRAC'
    p[0] = ['WFFRIP', p[2]]

def p_WFF1(p):
    'WFF : ID LBRAC expr RBRAC'
    p[0] = ['ATOM',p[1], p[3]]

def p_WFF_EXISTS(p):
    'WFF : LBRAC EXISTS expr1 RBRAC LBRAC WFF RBRAC'
    p[0] = ['EXISTS', p[3], p[6]]

def p_WFF_FORALL(p):
    'WFF : LBRAC FORALL expr1 RBRAC LBRAC WFF RBRAC'
    p[0] = ['FORALL', p[3], p[6]]

def p_WFF_NOTexpr(p):
    'WFF : NOT WFF'
    p[0] = ['NOT', p[2]]

def p_WFF_AND(p):
    'WFF : WFF AND WFF'
    p[0] = ['AND', p[1], p[3]]

def p_WFF_OR(p):
    'WFF : WFF OR WFF'
    p[0] = ['OR', p[1], p[3]]

def p_expr(p):
    'expr : expr COMMA value'
    p[0] = p[1] + [p[3]]

def p_exprExFo(p):
    'expr1 : expr1 COMMA value1'
    p[0] = p[1] + [p[3]]

def p_valueE(p):
    'expr1 : value1'
    p[0] = [p[1]]

def p_valu(p):
    'value1 : ID'
    p[0] = p[1]

def p_expr1(p):
    'expr : value'
    p[0] = ['value',p[1]]

def p_value(p):
    'value : NUMBER'
    p[0] = ['num', p[1]]

def p_value1(p):
    'value : STRING'
    p[0] = ['string', p[1]]

def p_value2(p):
    'value : ID'
    p[0] = ['id', p[1]]

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()