from flask import Flask, render_template, request, redirect
from random import randint
from datetime import datetime
import mysql.connector as mysql

app = Flask(__name__)

db = mysql.connect(host="localhost", database="bro", user="root", passwd="mypassword", auth_plugin="caching_sha2_password")
cursor = db.cursor()
cursor.execute("use bro;")

@app.route("/")
def hello():
    return render_template('HackGSUv1.html')

@app.route("/HackGSUv5", methods=['GET', 'POST'])
def HackGSUv5():
    return render_template("proflog.html")

@app.route("/Error", methods=['GET'])
def error():
    return render_template('Error.html')

@app.route("/test", methods=["GET", "POST"])
def authenticate():
    u_name = request.form["user"]
    pass_w = request.form["pass"]
    cursor.execute("select * from Professor where username=%s and password=%s;", (u_name, pass_w));
    records = cursor.fetchall()
    if len(records) != 0:
        return render_template("HackGSUv5.html")
    return render_template("proferror.html")

@app.route("/HackGSUv2", methods=['GET', 'POST'])
def HackGSUv2():
    if len(request.form) == 1:
        return hackGSUv2()
    if request.method == 'POST':
        #client_ip = request.remote_addr
        #cursor.execute("select * from Locations where ip=%s;", (client_ip,))
        #records = cursor.fetchall()
        #if len(records) == 0:
            #return render_template('Error.html')
        finame = request.form['name']
        laname = request.form['last']
        idno = request.form['ID']
        corn = request.form['courseID']
        now = datetime.now()
        daynowa = datetime.today().strftime('%A')
        x = now.strftime('%H:%M:%S')
        cursor.execute(f"select * from Information where id = {idno} and firstName=\"{finame}\" and lastName=\"{laname}\";")
        recos = cursor.fetchall()
        if len(recos) == 0:
            return render_template('HackGSUv3.html')
        if(len(recos) != 0):
            cursor.execute("select * from Attendees where id = %s and fname = %s and lname = %s and crn = %s;", (idno, finame, laname, corn,))
            qu = cursor.fetchall()
            if(len(qu) == 0):
                cursor.execute("select * from EnrolledCourses where id = %s and crn = %s;", (idno, corn))
                t1 = cursor.fetchall()
                if(len(t1) == 0):
                    return render_template('HackGSUv7.html')
                cursor.execute("select * from Courses where crn = %s and (day1 = %s or day2 = %s) and stime <= %s and etime >= %s;", (corn, daynowa, daynowa, x, x,))
                t2 = cursor.fetchall()
                if(len(t2) == 0):
                    return render_template('HackGSUv6.html')
                else:
                    cursor.execute("insert into Attendees (id, fname, lname, crn) values (%s, %s, %s, %s);", (idno, finame, laname, corn))
                    db.commit()
                    return render_template('HackGSUv2.html')
            else:
                return render_template('HackGSUv4.html')
        else:
            return render_template('HackGSUv3.html')

@app.route("/HackGSUv5.html", methods=['GET', 'POST'])
def heya():
    return render_template('HackGSUv5.html')

@app.route("/HackGSUv1", methods=['GET', 'POST'])
def hiya():
    return render_template('HackGSUv1.html')

@app.route("/HackGSUv1.html", methods=['GET', 'POST'])
def hey():
    return render_template('HackGSUv1.html')

@app.route("/HackGSUv2.html", methods=['GET', 'POST'])
def hackGSUv2():
    if request.method == 'POST':
        cran = request.form['crn']
        cursor.execute(f"select id, fname, lname from Attendees where crn = '{cran}';");
        records = cursor.fetchall()
        records = list(set(records))
        htmlcode = '''
        <html>
        <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width-device-width, intial-scale = 1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <style>
        body {
            background: url("https://github.com/preethampython101/EasyAttend-and-Diversify/blob/main/EasyAttend/Img-1.jpg?raw=true");
            background-repeat: no-repeat;
            background-size: 100%;
        }

        h1 {
            color: red;
            position: absolute;
            margin-left: 35%;
            margin-top: 3%;
            font-size: 3.0vw;
        }

        img {
            width: 15%;
            position: absolute;
            margin-left: 42%;
            margin-top: 2%;
        }

        a {
            display: inline-block;
            padding: 10px 20px;
            width: 15%;
            margin-top: 25%;
            margin-left: 40%;
            padding: 2.0%;
            color: #ebebeb;
            font-size: 2.5vw;
            font-family: Tahoma, Geneva, sans-serif;
            text-align: center;
            text-decoration: none;
            background: #c78cfa;
            border-radius: 15px;
            box-shadow: 10px 10px 10px #7228bd,
                -5px -5px 12px #9c4ced;
            text-shadow:
                0px 1px 3px rgba(000, 000, 000, 0.3),
                0px 0px 0px rgba(255, 255, 255, 0);
            position: absolute;
            clear: both;
            border: none;
            font-weight: strong;
        }

        a:hover {
            box-shadow: inset -3px -3px 3px rgba(255, 255, 255, 0.5),
                inset 5px 5px 5px rgba(0, 0, 0, 0.1);
        }

        table{
            margin-top: 8%;
            margin-left: 37%;
            position: absolute;
            background-color: #c78cfa;
        }
    </style>
    <title>Attendance ''' + ''' </title>
</head>
        <body>
        <h1>Attendance for ''' +cran+ '''</h1>
        <table border="2" cellspacing="2" cellpadding="2">
        <tr>
        <th><font face="Arial,Helvetica,sans-serif">ID</font></th>
        <th><font face="Arial,Helvetica,sans-serif">First Name</font></th>
        <th><font face="Arial,Helvetica,sans-serif">Last Name</font></th>
        </tr>
        '''
        for rec in records:
            htmlcode += '''<tr><td><font face="Arial, Helvetica, sans-serif">'''+str(rec[0])+'''</font></td>
            <td><font face="Arial, Helvetica, sans-serif">'''+rec[1]+'''</font></td>
            <td><font face="Arial, Helvetica, sans-serif">'''+rec[2]+'''</font></td>
            </tr>
            '''
        htmlcode += '''</table>
                        <a href="HackGSUv5" Method="GET" class="home">Go Back</a>
                       </body>
                       </html>
                    '''
        return htmlcode

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True, port=9999)
