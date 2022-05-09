from ply import lex

res_stuff = {"lambda": "LAMBDA", "fv": "FV", "alpha": "ALPHA"}

tokens = ["NUMBER","LPAREN","RPAREN","OP","NAME","LBRACKET","RBRACKET","EQUALS","COMMA","SEMI"] + list(res_stuff.values())

t_NUMBER = r"[0-9]+"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_OP = r"\+|\-|\*|\/"
t_LAMBDA = r"[Ll][Aa][Mm][Bb][Dd][Aa]"
t_LBRACKET = "\["
t_RBRACKET = "\]"
t_EQUALS = r"\="
t_FV = r"[Ff][Vv]"
t_ALPHA = r"[aA][lL][pP][hH][aA]"
t_COMMA = r"\,"
t_SEMI = r"\;"

def t_NAME(t):
    r"[a-zA-Z][a-zA-Z0-9]*"
    if t.value in res_stuff:
        t.type = res_stuff[t.value]
    return t

t_ignore = " \r\n\t"
t_ignore_COMMENT = r'\#.*'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()
