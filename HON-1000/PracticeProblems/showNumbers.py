def showNumbers(limit):
	for i in range(limit+1):
		if(i % 2 == 0):
			print(str(i) + " EVEN")
		else:
			print(str(i) + " ODD")

limit = int(input())

showNumbers(limit)