s = 10
def primeno(limit):
	for i in range(2, limit+1):
		for j in range(2, i):
			if(i % j == 0):
				break
		else:
			print(i)
			


limit = int(input())
s = 1
#print(2)
primeno(limit)
#Don't print outside when the function is void.