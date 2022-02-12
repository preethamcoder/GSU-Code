import traceback
from DLOGParser import parser

def main():
  while True:
    data = input("Enter Datalog rule: ")
    if data == 'exit':
      break
    try:
      if parser.parse(data):
        print("SAFE Datalog Rule")
      else:
        print("UNSAFE Datalog Rule")
    except Exception as err:
      print(err.args[0])
      traceback.print_tb(err.__traceback__)
      print("BAD STRING")
main()