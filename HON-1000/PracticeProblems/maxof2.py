def maxof2(a, b):
	if(a == b or a > b):
		return(a)
	else:
		return(b)
print("Enter the values of x and y one after the other.")

x = int(input())
y = int(input())

print("The larger number is " + str(maxof2(x, y)))
