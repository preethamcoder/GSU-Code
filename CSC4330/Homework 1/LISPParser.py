import ply.yacc as yacc
from LISPLexer import tokens

def p_begin(p):
  'begin : start SEMI'
  p[0] = p[1]

def p_st_1(p):
  'start : lisp'
  p[0] = ['lisp', p[1]]

def p_st_2(p):
  'start : boolean'
  p[0] = ['boolean',p[1]]

def p_st_3(p):
  'start : list'
  p[0] = ['list', p[1]]

def p_boolexp_1(p):
  '''boolean : TRUE
             | FALSE'''
  p[0] = ['boolean', p[1]]

def p_lispexp_1(p):
  'lisp : NUMBER'
  p[0] = ['num', p[1]]

def p_lispfrac1(p):
  'lisp : NUMBER DIV NUMBER'
  p[0] = ['frac', p[1], p[3]]

def p_lispexp_2(p):
  'lisp : LBRAC PLUS lisp lisp RBRAC'
  p[0] = ['+',p[3],p[4]]

def p_lispexp_3(p):
  'lisp : LBRAC MINUS lisp lisp RBRAC'
  p[0] = ['-',p[3],p[4]]

def p_lispexp_4(p):
  'lisp : LBRAC TIMES lisp lisp RBRAC'
  p[0] = ['*',p[3],p[4]]

def p_lispexp_5(p):
  'lisp : LBRAC DIV lisp lisp RBRAC'
  p[0] = ['/',p[3],p[4]]

def p_lispexp_6(p):
  'lisp : LBRAC IF boolean lisp lisp RBRAC'
  p[0] = ['if',p[3],p[4],p[5]]

def p_lispexp_7(p):
  'lisp : LBRAC CAR list RBRAC'
  p[0] = ['car', p[3]]

def p_boolexp_2(p):
  'boolean : BOOLEAN'
  p[0] = ['boolean', p[1]]

def p_boolexp_3(p):
  'boolean : LBRAC GT lisp lisp RBRAC'
  p[0] = ['>', p[3], p[4]]

def p_boolexp_4(p):
  'boolean : LBRAC LT lisp lisp RBRAC'
  p[0] = ['<', p[3], p[4]]

def p_boolexp_5(p):
  'boolean : LBRAC GE lisp lisp RBRAC'
  p[0] = ['>=', p[3], p[4]]

def p_boolexp_6(p):
  'boolean : LBRAC LE lisp lisp RBRAC'
  p[0] = ['<=', p[3], p[4]]

def p_boolexp_7(p):
  'boolean : LBRAC EQ lisp lisp RBRAC'
  p[0] = ['=', p[3], p[4]]

def p_boolexp_8(p):
  'boolean : LBRAC NE lisp lisp RBRAC'
  p[0] = ['<>', p[3], p[4]]

def p_boolexp_9(p):
  'boolean : LBRAC NE boolean RBRAC'
  p[0] = ['<>', p[3]]

def p_boolexp_10(p):
  'boolean : LBRAC AND boolean boolean RBRAC'
  p[0] = ['and', p[3], p[4]]

def p_boolexp_11(p):
  'boolean : LBRAC OR boolean boolean RBRAC'
  p[0] = ['or', p[3], p[4]]

def p_boolexp_12(p):
  'boolean : LBRAC NOT boolean RBRAC'
  p[0] = ['not' , p[3]]

def p_list_1(p):
  'list : LBRAC arr RBRAC'
  p[0] = ['list', p[2]]

def p_arrdec_1(p):
  'arr : arr lisp'
  p[0] = p[1] + [p[2]]

def p_arrdec_2(p):
  'arr : '
  p[0] = []

def p_list_2(p):
  'list : LBRAC CDR list RBRAC'
  p[0] = ['cdr', p[3]]

def p_list_3(p):
  'list : LBRAC CONS lisp list RBRAC'
  p[0] = ['cons', p[3], p[4]]

def p_error(p):
  print("Syntax error in input!")

parser = yacc.yacc()
