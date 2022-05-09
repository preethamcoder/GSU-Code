import ply.yacc as yacc
from lambdaNode import LambdaNod, OperationN
from lambdaLexer import tokens

def p_expr_start_0(p):
    "exprStart : expr SEMI"
    p[0] = OperationN("eval", p[1])

def p_expr_start_1(p):
    "exprStart : expr LBRACKET NAME EQUALS expr RBRACKET SEMI"
    p[0] = OperationN("sub", p[1], sub_var=p[3], sub_expr=p[5])

def p_expr_start_2(p):
    "exprStart : FV LBRACKET expr RBRACKET SEMI"
    p[0] = OperationN("fv", p[3])

def p_expr_start_3(p):
    "exprStart : ALPHA LBRACKET expr COMMA NAME RBRACKET SEMI"
    p[0] = OperationN("alpha", p[3], nay_nam=p[5])

def p_expr_0(p):
    "expr : NUMBER"
    p[0] = LambdaNod("number", value=p[1])

def p_expr_1(p):
    "expr : NAME"
    node = LambdaNod("var", name=p[1])
    node._free.add(p[1])
    p[0] = node

def p_expr_2(p):
    "expr : LPAREN expr expr RPAREN"
    node = LambdaNod("apply", opr=p[2], oprsa=p[3])
    node._free = p[2]._free.union(p[3]._free)
    p[0] = node

def p_expr_3(p):
    "expr : LPAREN LAMBDA NAME expr RPAREN"
    node = LambdaNod("lambda", bind=p[3], body=p[4])
    node._free = p[4]._free
    node._free.discard(p[3])
    p[0] = node

def p_expr_4(p):
    "expr : LPAREN OP expr expr RPAREN"
    node = LambdaNod("op", oprator=p[2], left=p[3], right=p[4])
    node._free = p[3]._free.union(p[4]._free)
    p[0] = node

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()
