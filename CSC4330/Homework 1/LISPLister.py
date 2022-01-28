import ply.lex as lex

reserved = {'car' : 'CAR', 'cdr' : 'CDR', 'if' : 'IF', 'or' : 'OR', 'and' : 'AND', 'cons' : 'CONS', 'true' : 'TRUE', 'false' : 'FALSE', 'not' : 'NOT'}
tokens = ['BOOLEAN', 'NUMBER','LBRAC','RBRAC','SEMI','PLUS','MINUS','TIMES', 'DIV', 'GT', 'GE', 'LT', 'LE', 'EQ', 'NE'] + list(reserved.values())

t_TRUE  = r'[tT][rR][uU][eE]'
t_FALSE = r'[fF][aA][lL][sS][eE]'
t_LBRAC = r'\('
t_RBRAC = r'\)'
t_SEMI  = r'\;'
t_IF    = r'[iI][fF]'
t_PLUS  = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIV   = r'/'
t_AND   = r'[aA][nN][dD]'
t_OR    = r'[oO][rR]'
t_CAR   = r'[cC][aA][rR]'
t_CDR   = r'[cC][dD][rR]'
t_GT    = r'\>'
t_GE    = r'\>='
t_LT    = r'\<'
t_LE    = r'\<='
t_EQ    = r'\='
t_NE    = r'\<>'
t_CONS  = r'[cC][oO][nN][sS]'
t_NOT   = r'[nN][oO][tT]'

def t_NUMBER(t):
        r'[-+]?[0-9]+(\.([0-9]+)?)?'
        t.value = float(t.value)
        t.type  = 'NUMBER'
        return t

def t_ID(t):
        r'[a-zA-Z][_a-zA-Z0-9]*'
        t.type = reserved.get(t.value.lower(),'ID')
        return t

t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'

def t_error(t):
        print(f"Illegal character {t.value[0]}")
        raise Exception('LEXER ERROR')

lexer = lex.lex()
