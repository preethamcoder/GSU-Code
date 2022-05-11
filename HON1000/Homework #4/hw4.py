import mysql.connector as mysql

def print_room_details(db,bcode,rnum):
  cursor = db.cursor()
  q = '''select building.bname, room.rnumber, room.bcode, sum(cap), layout, type, dept from ROOM, building where building.bcode = %s and room.rnumber = %s and room.bcode = building.bcode;'''
  val = (bcode, rnum);
  cursor.execute(q, val);
  rec = cursor.fetchall()
  result = {'bldg\t': rec[0][0] + " ("+bcode+")", 'rnumber\t': rnum, 'cap\t': rec[0][3], 'layout\t': rec[0][4], 'type\t': rec[0][5], 'dept\t': rec[0][6]}
  for i in result:
    print(i, result[i])
  #for row in rec:
   # for element in row:
    #    print(element)
    
def print_rooms_with_cap(db,cap_lower,cap_upper):
  cursor = db.cursor()
  q = '''select DISTINCT(room.bcode), room.rnumber, cap from room, building where cap > %s and cap < %s;'''
  val = (cap_lower, cap_upper)
  cursor.execute(q, val);
  rec = cursor.fetchall()
  for row in rec:
    for element in row:
      print(element, end = '\t')
    print()

def update_room_cap(db,bcode,rnum,cap):
  cursor = db.cursor()
  q = '''update room set cap = %s where room.bcode = %s and room.rnumber = %s;'''
  val = (cap, bcode, rnum)
  cursor.execute(q, val);
  print("Room details updated")
def main():
  # please update database, user, and passwd to suit your database
  db = mysql.connect(
    host="localhost",
    database="db102",
    user="root",
    passwd="Passw0rd$",
    auth_plugin='mysql_native_password'
  )
  print()
  while True:
    s = input("r b:r, c n:m, u b:r:n, q for quit: ")
    if s[0] == 'r':
      room = s[1:].strip().split(":")
      bcode = room[0]
      rnum = room[1]
      print_room_details(db,bcode,rnum)
    elif s[0] == 'c':
      caps = s[1:].strip().split(":")
      cap_lower = int(caps[0])
      cap_upper = int(caps[1])
      print_rooms_with_cap(db,cap_lower,cap_upper)
    elif s[0] == 'u':
      room = s[1:].strip().split(":")
      bcode = room[0]
      rnum = room[1]
      cap = int(room[2])
      update_room_cap(db,bcode,rnum,cap)
    elif s[0] == 'q':
      break
    else:
      print("Invalid option")
  db.close()

main()