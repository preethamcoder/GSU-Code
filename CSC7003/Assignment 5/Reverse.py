from Stack import *
def main():
    inp = input("Enter a string (q to quit): ")
    while(inp != 'q'):
        S = Stack()
        for i in inp:
            S.push(i)
        rev = ""
        for i in range(len(inp)):
            rev += S.pop()
        print("Reversed string is: ", rev)
        inp = input("Enter a string (q to quit): ")
main()