from WFFParser import parser
results = []

def eval_expression(tree):
  if tree[0] == 'value':
      lenof(tree)
  elif tree[0] == 'WFF' or tree[0] == 'WFFRIP' or tree[0] == 'NOT':
    eval_expression(tree[1])
  elif tree[0] == 'ATOM':
    eval_expression(tree[2])
  elif tree[0] == 'EXISTS' or tree[0] == 'FORALL':
    eval_expression(tree[2])
    comparearrays(existsfor(tree[1]), results)
  elif tree[0] == 'AND' or tree[0] == 'OR':
    eval_expression(tree[1])
    eval_expression(tree[2])
    strain(results)
  else:
    return

def existsfor(tree):
  arr = []
  tar = 0
  while len(tree)-1 >= tar:
    v1 = tree[tar]
    arr.append(v1)
    tar += 1
  return arr

def strain(arr):
  arr1 = list(dict.fromkeys(arr))
  arr.clear()
  each = 0
  while len(arr1)-1 >= each:
    arr.append(arr1[each])
    each += 1
  return arr1

def comparearrays(arr, arr1):
  for each in arr:
    while each in arr1: 
      arr1.remove(each)

def lenof(tree):
  tar = 0
  while len(tree)-1 >= tar:
    if (tree[tar][0]) == 'id':
      v1 = tree[tar][1]
      results.append(v1)
    tar += 1
  strain(results)

def freevars(tree):
  eval_expression(tree)

def read_input():
  result = ''
  while True:
    data = input('WFF: ').strip() 
    if ';' in data:
      results.clear()
      i = data.index(';')
      result += data[0:i+1]
      break
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
      freevars(tree[1])
    except Exception as inst:
      continue
    try:
      if not results:
        print('\nCLOSED WFF\n')
      else:
        print(f'\nOPEN WFF with Free Variables: {results}', end= "")
        print()
    except Exception as inst:
      print(inst.args[0])
 
main()