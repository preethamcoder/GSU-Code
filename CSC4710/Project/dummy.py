import mysql.connector as mysql
res = []
db = mysql.connect(host="localhost", database="bro", user="root", passwd="mypassword", auth_plugin="caching_sha2_password")
cursor = db.cursor()
idno = 2000121193
for each in res:
	print(each)
for rec in cursor:
	res.append(rec)
finame = "Preetham"
laname = "Thelluri"
crn = "ECON2105"
if len(res) != 0:
	cursor.execute(f"select * from Attendees where id = {idno} and fname='{finame}' and lname='{laname}' and crn='{crn}';")
	res = []
	for rec in cursor:
		res.append(rec)
	print(res)

#Building serverless webapp on AWS services
