def fizz_buzz(x):
	if(x % 15 == 0):
		return("FizzBuzz")
	elif(x % 3 == 0):
		return("Fizz")
	elif(x % 5 == 0):
		return("Buzz")
	else:
		return(str(x))

print("Enter the number")
a = int(input())

print(fizz_buzz(a))