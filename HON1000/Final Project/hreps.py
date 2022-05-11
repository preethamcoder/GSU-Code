import mysql.connector as mysql
db = mysql.connect(
    host="localhost",
    database="db100",
    user="root",
    passwd="Passw0rd$",
    auth_plugin='mysql_native_password'
  )
cursor = db.cursor()
f = open("C:\\Users\\sthelluri1\\Desktop\\hreps.csv",'r')
lines = f.readlines()
x = 0
for i in lines:
    x += 1
    a = i.split(',')
    a[len(a)-1] = a[len(a)-1][0:-1]
    idc = x
    ln = a[0]
    fn = a[1]
    bd = a[2]
    gn = a[3]
    st = a[4]
    ds = a[5]
    pt = a[6]
    ur = a[7]
    tw = a[8]
    fb = a[9]
    yt = a[10]
    #print('''insert into HREP values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''',(idc, ln, fn, bd, gn, st, ds, pt, ur, tw, fb, yt))
    cursor.execute('''insert into HREP values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''',(idc, ln, fn, bd, gn, st, ds, pt, ur, tw, fb, yt))
db.commit()
