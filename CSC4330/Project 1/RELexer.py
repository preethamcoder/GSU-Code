import ply.lex as lex

tokens = ['LBRAC','RBRAC','SEMI','PLUS','STAR', 'LETTER', 'EPSILON']

t_SEMI = r'\;'
t_LBRAC = r'\('
t_RBRAC = r'\)'
t_STAR = r'\*'
t_LETTER = r'[a-zA-Z0-9]'
t_PLUS = r'\+'
t_EPSILON = r'\^'

"""def t_LETTER(t):
        r'[a-zA-Z0-9]'
        t.value = string(t.value)
        t.type = 'LETTER'
        return t
"""
def t_error(t):
        print(f"Illegal character {t.value[0]}")
        raise Exception('LEXER ERROR')

lexer = lex.lex()
