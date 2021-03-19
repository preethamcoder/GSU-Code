import math
def speedLim(speed):
	if(speed <= 70):
		return("Ok")
	elif(speed > 130):
		return("License suspended")
	else:
		x = int(math.floor((speed - 70)/5))
		return("Points: " + str(x))
speed = int(input())
print(speedLim(speed))