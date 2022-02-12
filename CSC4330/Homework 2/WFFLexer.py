import ply.lex as lex

reserved = {'and' : 'AND', 'or' : 'OR', 'not' : 'NOT', 'exists' : 'EXISTS', 'forall' : 'FORALL'}
tokens = ['SEMI', 'ID', 'COMMA', 'LBRAC', 'RBRAC', 'NUMBER', 'STRING'] + list(reserved.values())

t_SEMI  = r'\;'
t_COMMA = r'\,'
t_LBRAC = r'\('
t_RBRAC = r'\)'
t_AND   = r'[aA][nN][dD]'
t_OR    = r'[oO][rR]'
t_NOT   = r'[nN][oO][tT]'
t_EXISTS = r'[eE][xX][iI][sS][tT][sS]'
t_FORALL = r'[fF][oO][rR][aA][lL][lL]'

def t_NUMBER(t):
        r'[-+]?[0-9]+(\.([0-9]+)?)?'
        t.value = float(t.value)
        t.type  = 'NUMBER'
        return t

def t_ID(t):
        r'[a-z][_a-zA-Z0-9]*'
        t.type = reserved.get(t.value.lower(),'ID')
        return t

def t_STRING(t):
        r"\'[a-zA-Z][_a-zA-Z0-9]*\'"
        t.type = 'STRING'
        return t
        
t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'

def t_error(t):
        print(f"Illegal character {t.value[0]}")
        raise Exception('LEXER ERROR')

lexer = lex.lex()