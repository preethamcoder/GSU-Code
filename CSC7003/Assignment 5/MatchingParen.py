from Stack import *
def is_matched(expr):
    S = Stack()
    T = Stack()
    for i in expr:
        if(i == "(" or i == "{" or i == "["):
            S.push(i)
        elif(i == ")" or i == "}" or i == "]"):
            T.push(i)
    op = ""
    for i in range(S.__len__()):
        op += S.pop()
    op_cn = op.count("(")
    op_cn1 = op.count("{")
    op_cn2 = op.count("[")
    cl_cn = T.__str__().count(")")
    cl_cn1 = T.__str__().count("}")
    cl_cn2 = T.__str__().count("]")    
    if(op_cn == cl_cn and op_cn1 == cl_cn1 and op_cn2 == cl_cn2):
        return("BALANCED")
    else:
        return("NOT BALANCED")
def main():
    inp = input("Enter a series of brackets (q to quit): ")
    while(inp != 'q'):
        print(is_matched(inp))
        inp = input("Enter a series of brackets (q to quit): ")
main()