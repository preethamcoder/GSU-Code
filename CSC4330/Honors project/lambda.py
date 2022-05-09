from lambdaNode import LambdaNod, OperationN
from lambdaParser import parser

# too many ifs down there, I reckon....should probably do that more efficiently
def main():
  while True:
    stuff = input("LAMBDA> ")
    if stuff == 'exit;':
      break
    try:
        op_tree = parser.parse(stuff)
    except Exception as inst:
        print(inst.args[0])
        continue
    try:
        if op_tree:
            end_prod(op_tree)
    except Exception as e:
        print(e.args[0])

# Can you please work, friendly method?!?!
def end_prod(op_tree):
    if op_tree._kind == "fv":
        print(f'Free variables: {op_tree._lambda._free}')
    elif op_tree._kind == "alpha":
        if op_tree._lambda.type != "lambda":
            print(op_tree._lambda)
        past_guy = op_tree._lambda._bind
        work_guy = op_tree._naya
        lam_exptree = op_tree._lambda
        if lam_exptree._bind == past_guy:
            lam_exptree._bind = work_guy
            mod_alp(lam_exptree._body, past_guy, work_guy)
        print(lam_exptree)
    elif op_tree._kind == "sub":
        op_tree._lambda = rep_da_subs(op_tree._lambda, op_tree._sub_var, op_tree._sub_expr)
        print(op_tree._lambda)
    elif op_tree._kind == "eval":
        eval_it_down(op_tree._lambda)

# Time to break dis thing down, BOXED
def eval_it_down(op_tree):
    nextttt = True
    while(nextttt):
        print(op_tree)
        modifs, op_tree = beat_it_down_beta(op_tree)
        nextttt = modifs

# SMASHED
def beat_it_down_beta(op_tree):
    modifs = False
    if op_tree.type == "number":
        modifs = False
    elif op_tree.type == "var":
        modifs = False
    elif op_tree.type == "op":
        if op_tree._right.type == op_tree._left.type == "number":
            op_tree = oper(op_tree._oprator, op_tree._left._value, op_tree._right._value)
            modifs = True
        else:
            if not (op_tree._left.type == "number" or op_tree._left.type == "var"):
                chngv1, op_tree._left = beat_it_down_beta(op_tree._left)
                modifs = chngv1 or modifs
            elif not (op_tree._right.type == "number" or op_tree._right.type == "var"):
                chngv2, op_tree._right = beat_it_down_beta(op_tree._right)
                modifs = chngv2 or modifs
    elif op_tree.type == "apply":
        if op_tree._opr.type == "lambda":
            op_tree = rep_da_subs(op_tree._opr._body, op_tree._opr._bind, op_tree._oprsa)
            modifs = True
        else:
            if not (op_tree._opr.type == "number" or op_tree._opr.type == "var"):
                chngv1, op_tree._opr = beat_it_down_beta(op_tree._opr)
                modifs = chngv1 or modifs
            elif not (op_tree._oprsa.type == "number" or op_tree._oprsa.type == "var"):
                chngv2, op_tree._oprsa = beat_it_down_beta(op_tree._oprsa)
                modifs = chngv2 or modifs
    elif op_tree.type == "lambda":
        if not (op_tree._body.type == "number" or op_tree._body.type == "var"):
            chngv, op_tree._body = beat_it_down_beta(op_tree._body)
            modifs = chngv or modifs
    if modifs is None:
        modifs = False
    return modifs, op_tree

def oper(op, left, right):
    if op == "+":
        return LambdaNod("number", value=left + right)
    elif op == "-":
        return LambdaNod("number", value=left - right)
    elif op == "/":
        return LambdaNod("number", value=left / right)
    elif op == "*":
        return LambdaNod("number", value=left * right)

def mod_alp(body, past_guy, work_guy):
    if body.type == "var":
        if body._name == past_guy:
            body._name = work_guy
    elif body.type == "lambda":
        if body._bind == past_guy:
            body._bind = work_guy
        mod_alp(body._body, past_guy, work_guy)
    elif body.type == "apply":
        mod_alp(body._opr, past_guy, work_guy)
        mod_alp(body._oprsa, past_guy, work_guy)
    elif body.type == "op":
        mod_alp(body._left, past_guy, work_guy)
        mod_alp(body._right, past_guy, work_guy)

# Come on method, why you gotta keep dying -- need to fix more bugs here
def rep_da_subs(op_tree, replaced_var, xpresson):
    if op_tree.type == "number":
        return op_tree
    elif op_tree.type == "var":
        return xpresson if op_tree._name == replaced_var else op_tree
    elif op_tree.type == "apply":
        op_tree._opr = rep_da_subs(op_tree._opr, replaced_var, xpresson)
        op_tree._oprsa = rep_da_subs(op_tree._oprsa, replaced_var, xpresson)
        return op_tree
    elif op_tree.type == "op":
        op_tree._left = rep_da_subs(op_tree._left, replaced_var, xpresson)
        op_tree._right = rep_da_subs(op_tree._right, replaced_var, xpresson)
        return op_tree
    elif op_tree.type == "lambda":
        if op_tree._bind != replaced_var:
            if op_tree._bind in xpresson._free:
                mod_alp(op_tree, op_tree._bind, f"{op_tree._bind}'")
            op_tree._body = rep_da_subs(op_tree._body, replaced_var, xpresson)
        return op_tree

main()