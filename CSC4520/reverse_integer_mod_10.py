def reverse_digit(inp):
    if(inp == 0):
         return 0
    else:
        rev = 0
        if(inp < 0):
            while(inp != 0):
                rev += inp % 10
                if(inp > 9):
                    rev *= 10
                inp = inp // 10
            return (rev * -1)
        else:
            while(inp != 0):
                rev += inp % 10
                if(inp > 9):
                    rev *= 10
                inp = inp // 10
            return rev

if __name__ == '__main__':
	num = int(input("Enter the number you want to reverse: "))
	reverse = reverse_digit(num)
	print(reverse)
