from LISPParser import parser

#evaluating the expressions to make sure every thing is covered
def eval_expression(tree):
#returning ids or output based on input/recursive call
    if tree[0] == 'num':
        return tree[1]
    if tree[0] == 'boolean':
        return tree[1]
    if tree[0] == 'frac':
        sfrac = str(float(tree[1])) + '/' + str(float(tree[2]))
        return sfrac
    #Arithmetic department
    elif tree[0] == '+' or tree[0] == '-' or tree[0] == '*' or tree[0] == '/':
        v1 = eval_expression(tree[1])
        if isinstance(v1,str):
            return v1
        v2 = eval_expression(tree[2])
        if isinstance(v2,str):
            return v2
        if tree[0] == '+':
            return v1+v2
        elif tree[0] == '-':
            return v1-v2
        elif tree[0] == '*':
            return v1*v2
        elif v2 != 0:
            return v1/v2
        else:
            return 'Divide by Zero'
    #Conditional department
    elif tree[0] == 'if':
        v1 = evalBool(tree[1])
        v2 = eval_expression(tree[2])
        v3 = eval_expression(tree[3])
        if v1:
            return v2
        else:
            return v3
    #Pop first department
    elif tree[0] == 'car':
        arr = evalList(tree[1])
        if len(arr) < 1:
            return 'Cannot CAR empty things!'
        if isinstance(arr,str):
            return arr
        else:
            v1 = arr[0]
            return v1

#Boolean department
def evalBool(tree):
    if tree[0] == 'boolean':
        return tree[1]
    elif tree[0] == '>' or tree[0] == '<' or tree[0] == '>=' or tree[0] == '<=' or tree[0] == '=' or tree[0] == '<>':
        v1 = eval_expression(tree[1])
        if isinstance(v1,str):
            return v1
        v2 = eval_expression(tree[2])
        if isinstance(v2,str):
            return v2
        if tree[0] == '>':
            return v1>v2
        elif tree[0] == '<':
            return v1<v2
        elif tree[0] == '>=':
            return v1>=v2
        elif tree[0] == '<=':
            return v1<=v2
        elif tree[0] == '=':
            return v1==v2
        elif tree[0] == '<>':
            return(v1 > v2 or v1 < v2)
        else:
            return 'Error in your input'
    elif tree[0] == tree[0] == 'and' or tree[0] == 'or' or tree[0] == 'not':
        v1 = evalBool(tree[1])
        if isinstance(v1,str):
            return v1
        if tree[0] == 'not':
            return not v1
        v2 = evalBool(tree[2])
        if isinstance(v2,str):
            return v2
        elif tree[0] == 'and':
            return v1 and v2
        elif tree[0] == 'or':
            return v1 or v2
        else:
            return 'Error in input'

#List department
def evalList(tree):
    if tree[0] == 'list':
        cap = 0
        arr = []
        while ((len(tree[1])-1) >= cap):
            v1 = eval_expression(tree[1][cap])
            arr.append(v1)
            cap += 1
        return arr
    #Everything but first element is returned
    if tree[0] == 'cdr':
        arr = evalList(tree[1])
        if len(arr) < 1:
            return 'Cannot CDR on an empty list!'
        else:
            arr = arr[1:]
            return arr
    if tree[0] == 'cons':
        arr = evalList(tree[2])
        v2 = eval_expression(tree[1])
        arr.insert(0, v2)
        return arr

def read_input():
  res = ''
  while True:
    data = input('LISP: ').strip()
    if ';' in data:
      tar_ind = data.index(';')
      res += data[0:tar_ind+1]
      break
  return res

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
        answer = ''
        try:
            if tree[0] == 'lisp':
                answer = eval_expression(tree[1])
            if tree[0] == 'boolean':
                answer = (evalBool(tree[1]))
                if(answer == "True"):
                    answer = True
                elif(answer == "False"):
                    answer = False
            if tree[0] == 'list':
                answer = evalList(tree[1])
            if isinstance(answer,str):
                if tree[0] == 'lisp' and tree[1][0] == 'frac':
                    print('\n'+str(answer)+'\n')
                else:
                    print('\n'+answer+'\n')
            else:
                if tree[0] == 'list':
                   print('\n'+ str(answer).replace('[', '(').replace(']', ')')+'\n')
                else:
                    print('\n'+str(answer)+'\n')
        except Exception as inst:
            print(inst.args[0])
main()
