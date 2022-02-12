import ply.lex as lex

reserved = {'not' : 'NOT', 'reg' : 'REG'}
tokens = ['DOT', 'ID', 'COMMA', 'LBRAC', 'RBRAC', 'NUMBER'] + list(reserved.values())

t_COMMA = r'\,'
t_LBRAC = r'\('
t_RBRAC = r'\)'
t_DOT = r'\.'
t_NOT = r'[nN][oO][tT]'
t_REG = r':-'

def t_NUMBER(t):
        r'[-+]?[0-9]+(\.([0-9]+)?)?'
        t.value = float(t.value)
        t.type  = 'NUMBER'
        return t

def t_ID(t):
        r'[a-z][_a-zA-Z0-9]*'
        t.type = reserved.get(t.value.lower(),'ID')
        return t
        
t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'

def t_error(t):
        print(f"Illegal character {t.value[0]}")
        raise Exception('LEXER ERROR')

lexer = lex.lex()