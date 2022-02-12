import mysql.connector as mysql
db = mysql.connect(
    host="localhost",
    database="db100",
    user="root",
    passwd="Passw0rd$",
    auth_plugin='mysql_native_password'
  )
cursor = db.cursor()
f = open("C:\\Users\\sthelluri1\\Desktop\\senators.txt",'r')
lines = f.readlines()
x = 0
for i in lines:
    a = i.split(',')
    x += 1
    a[len(a)-1] = a[len(a)-1][0:-1]
    idc = x
    ln = a[0]
    fn = a[1]
    bd = a[2]
    gn = a[3]
    st = a[4]
    pt = a[5]
    ur = a[6]
    tw = a[7]
    fb = a[8]
    yt = a[9]
    #print('''insert into SENATOR values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''',(idc, ln, fn, bd, gn, st, pt, ur, tw, fb, yt))
    cursor.execute('''insert into SENATOR values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''',(idc, ln, fn, bd, gn, st, pt, ur, tw, fb, yt))
db.commit()
