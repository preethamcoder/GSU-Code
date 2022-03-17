from REParser import parser
from RENode import RENode
import queue

global count
count = 1

def regular_expressions(tree):
    
    
    calc_unique_numbers(tree)
    alphabet = calc_alphabet(tree,{})

    calc_nullable(tree)
    calc_firstpos(tree)
    calc_lastpos(tree)
    followpos = dict(sorted(calc_followpos(tree,{}).items()))
    return calc_DFA(tree, followpos, alphabet)

def calc_alphabet(tree, alphabet):
    if tree._lchild:
        calc_alphabet(tree._lchild,alphabet)
    if tree._rchild:
        calc_alphabet(tree._rchild,alphabet)
    if tree._operator == 'leaf':
        if tree._symbol == '^' or tree._symbol == '#':
            pass
        else:
            if tree._symbol not in alphabet:
                alphabet[tree._symbol] = set()
                alphabet[tree._symbol].add(tree._position)
            else:
                alphabet[tree._symbol].add(tree._position)
    return alphabet

def calc_unique_numbers(tree):
    global count
    if tree._lchild:
        calc_unique_numbers(tree._lchild)
    if tree._rchild:
        calc_unique_numbers(tree._rchild)  

    if tree._operator == 'leaf':
        if tree._symbol == '^':
            pass
        else:
            tree._position = count
            count += 1

     
    
def calc_nullable(tree):
    if tree._lchild:
        calc_nullable(tree._lchild)

    if tree._rchild:
        calc_nullable(tree._rchild) 

    if tree._operator == 'leaf':
        if tree._symbol == '^':
            tree._nullable = True
        else:
            tree._nullable = False
    elif tree._operator == '+':
        tree._nullable = tree._lchild._nullable or tree._rchild._nullable
    elif tree._operator == '.':
        tree._nullable = tree._lchild._nullable and tree._rchild._nullable
    elif tree._operator == '*':
        tree._nullable = True

def calc_firstpos(tree):
    if tree._lchild:
        calc_firstpos(tree._lchild)

    if tree._rchild:
        calc_firstpos(tree._rchild)

    if tree._operator == 'leaf':
        if tree._symbol == '^':
            tree._firstpos = set()
        else:
            tree._firstpos.add(tree._position)
    elif tree._operator == '+':
        tree._firstpos = tree._lchild._firstpos.union(tree._rchild._firstpos)
    elif tree._operator == '.':
        if tree._lchild._nullable:
            tree._firstpos = tree._lchild._firstpos.union(tree._rchild._firstpos)
        else:
            tree._firstpos = tree._lchild._firstpos
        
    elif tree._operator == '*':
        tree._firstpos = tree._lchild._firstpos

def calc_lastpos(tree):
    if tree._lchild:
        calc_lastpos(tree._lchild)

    if tree._rchild:
        calc_lastpos(tree._rchild)

    if tree._operator == 'leaf':
        if tree._symbol == '^':
            tree._lastpos = set()
        else:
            tree._lastpos.add(tree._position)
    elif tree._operator == '+':
        tree._lastpos = tree._lchild._lastpos.union(tree._rchild._lastpos)
    elif tree._operator == '.':
        if tree._rchild._nullable:
            tree._lastpos = tree._lchild._lastpos.union(tree._rchild._lastpos)
        else:
            tree._lastpos = tree._rchild._lastpos
        
    elif tree._operator == '*':
        tree._lastpos = tree._lchild._lastpos

def calc_followpos(tree, followpos):
    if tree._lchild:
        calc_followpos(tree._lchild, followpos)

    if tree._rchild:
        calc_followpos(tree._rchild, followpos)
        
    if tree._operator == '.':
        for i in tree._lchild._lastpos:
            if i not in followpos:
                followpos[i] = set()

            followpos[i] = followpos[i].union(tree._rchild._firstpos)
        
    elif tree._operator == '*':
        for i in tree._lastpos:
            if i not in followpos:
                followpos[i] = set()
            followpos[i] = followpos[i].union(tree._firstpos)

    elif tree._symbol == '#':
        followpos[tree._position] = set()
    else:  
        pass

    return followpos

def calc_DFA(tree, followpos, alphabet):
    dfa = dict()
    marked = list()
    position_of_hash = 1
    for i in followpos:
        if i > position_of_hash:
            position_of_hash = i
    start_state = tree._firstpos
    states = queue.Queue()
    states.put(start_state)
    print(f'start_state({start_state}).')
    already_printed = set()
    while states.empty() == False:
        T = states.get()
        marked.append(T)
        dfa[str(T)] = dict()
        for symbol in alphabet:
            U = set()
            for p in T:
                if p in alphabet[symbol]:
                    U = U.union(followpos[p])
            if len(U) != 0 and U not in marked:
                states.put(U)
            dfa[str(T)][symbol] = U
            to_print = f"delta({T},{symbol},{U})."
            if to_print in already_printed:
                pass
            else:
                print(to_print)
                already_printed.add(to_print)
    dfa["{}"] = dict()
    for char in alphabet:
        print(f"delta(set(),{char},set()).")
        dfa["{}"][char] = "{}"
    for state in dfa:
        if str(position_of_hash) in state:
            print(f"final_state({state}).")
    return dfa, str(start_state)

def calc_match(start_state, dfa, string):
    curr_state = start_state
    if string == '':
        return "NO MATCH"
    for char in string:
        if curr_state == '{}' or curr_state == 'set()':
            return "NO MATCH"
        if char not in dfa[curr_state]:
            print(dfa[curr_state])
            return "NO MATCH"
        new_state = str(dfa[curr_state][char]) 
        curr_state = new_state
        if curr_state == '{}' or curr_state == 'set()':
            return "NO MATCH"
    return "MATCH"


def read_input():
    result = ''
    while True:
        data = input('REGEX: ').strip()
        if ';' in data:
            i = data.index(';')
            result += data[0:i+1]
            break
        else:
            result += data + ' '
    return result

def read_string():
    result = ''
    while True:
        data = input('INPUT STRING: ').strip()
        if ';' in data:
            i = data.index(';')
            result += data[0:i+1]
            break
        else:
            result += data + ' '
    return result


def main():
    while True:
        data = read_input()
        if data == 'exit;':
            break
        try:
            tree = parser.parse(data)
        except Exception as inst:
            print(inst.args[0])
            continue
        try:
            global count
            count = 1
            answer,start_state = regular_expressions(tree)
            print('*'*10)
            print(answer)
            print(start_state)
            print('*'*10)
            print(tree)
            while True:
                string = read_string()
                if string == 'exit;':
                    break
                string = string.strip(';')
                print(calc_match(start_state, answer, string))
           
            if isinstance(answer, str):
                print('\nEVALUATION ERROR: '+answer+'\n')
            else:
                pass                   

        except Exception as inst:
            print(inst.args[0])


main()
