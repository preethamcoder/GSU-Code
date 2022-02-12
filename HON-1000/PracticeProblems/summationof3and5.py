def summation(limit):
	sum = 0
	for i in range(limit):
		if(3*i <= limit):
			sum += (3*i)
		if(5*i <= limit):
			sum += (5*i)
		if(15*i <= limit):
			sum -= (15*i)
	print(sum)
limit = int(input())
summation(limit)