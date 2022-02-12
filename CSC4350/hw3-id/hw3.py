import math
import os

def q1(inp):
	v_count = (inp.lower().count('a') + inp.lower().count('e') + inp.lower().count('i') + inp.lower().count('o') + inp.lower().count('u'))
	c_count = len(inp)-v_count
	if(v_count > c_count):
		return True
	elif(v_count < c_count):
		return False
	else:
		return None

def q2(radius, height):
	return(math.pi * radius * radius * height)

def q3(lst):
	res = ','.join(lst)
	return(res)

def q4(nest_lst):
	output = open("output.csv", "w")
	for row in nest_lst:
		res = q3(row)
		output.write(res+'\n')
	output.close()
	return(os.path.abspath('output.csv'))

def q5(fname):
	inp = open(fname, 'r')
	data = inp.readlines()
	out = []
	for each in data:
		each = each.replace("\n", "")
		out.append(each.split(","))
	return out

def q6(n1, n2):
	try:
		print(n1/n2)
		return
	except ZeroDivisionError:
		print("You cannot divide a number by 0")
		return

def q7(integers):
	return(list(set(integers)))

def q8():
	os.system('mkdir hw3-folder')
	return
