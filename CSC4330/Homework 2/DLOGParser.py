import ply.yacc as yacc
from DLOGLexer import tokens

def p_dlog_start_0(p):
    "dlog_start : dlog DOT"
    p[0] = p[1]

def p_dlog_0(p):
    "dlog : left REG right"
    p[0] = ''
    if(p[1].symmetric_difference(p[3])):
        p[0] = False
    else:
        p[0] = True 

def p_lhs_0(p):
    "left : form"
    lhs_vars = set(p[1])
    p[0] = lhs_vars

def p_rhs_0(p):
    "right : form2"
    rhs_vars = set()
    for varlist in p[1]:
        if varlist:
            rhs_vars = rhs_vars.union(set(varlist))
    p[0] = rhs_vars

def p_formseq_0(p):
    "form2 : form COMMA form2"
    p[0] = [p[1]] + p[3]

def p_formseq_1(p):
    "form2 : negation COMMA form2"
    p[0] = [p[1]] + p[3]

def p_formseq_2(p):
    "form2 : form"
    p[0] = [p[1]]

def p_formseq_3(p):
    "form2 : negation"
    p[0] = [p[1]]

def p_form_0(p):
    "form : predicate LBRAC argument2 RBRAC"
    p[0] = p[3]

def p_negform_0(p):
    "negation : NOT form"
    p[0] = None

def p_argseq_0(p):
    "argument2 : argument COMMA argument2"
    p[0] = [p[1]] + p[3]

def p_argseq_1(p):
    "argument2 : argument"
    p[0] = [p[1]]

def p_pred_0(p):
    "predicate : ID"
    p[0] = None

def p_arg_0(p):
    "argument : ID"
    p[0] = p[1]

def p_arg_1(p):
    "argument : NUMBER"
    p[0] = None

def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()