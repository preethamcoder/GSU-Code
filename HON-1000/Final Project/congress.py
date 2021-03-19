from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
import mysql.connector as mysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db = mysql.connect(
  host="localhost",
  database="db100",
  user="root",
  passwd="Passw0rd$",
  auth_plugin='mysql_native_password'
)

@app.route('/congress/senator/party/<party>', methods=['GET'])
def get_senators_by_party(party):
  query = '''
    select state, fname, lname, concat(DAY(birthday),' ',MONTHNAME(birthday), ' ', YEAR(birthday)) birthday, url, twitter, facebook, youtube
    from SENATOR
    where party = %s
    order by state
  '''
  cursor = db.cursor()
  cursor.execute(query,(party,))
  records = cursor.fetchall()
  if len(records) == 0:
    abort(404)
  senators = []
  for record in records:
    senators.append({'state':record[0], 'fname':record[1], 'lname':record[2],
                  'birthday':record[3],
                  'url':record[4], 'twitter':record[5], 'facebook':record[6],
                  'youtube':record[7]})

  result = {'senators':senators}
  cursor.close()
  return jsonify(result)

@app.route('/congress/hrep/<state_code>/<district>', methods=['GET'])
def get_hreps_by_district(state_code,district):
  query = '''
    select fname, lname, concat(DAY(birthday),' ',MONTHNAME(birthday), ' ', YEAR(birthday)) birthday, url, twitter, facebook, youtube
    from HREP
    where state = %s and district = %s
  '''
  cursor = db.cursor()
  cursor.execute(query,(state_code,district))
  records = cursor.fetchall()
  if len(records) == 0:
    abort(404)
  result = {'fname':records[0][0], 'lname':records[0][1], 'birthday':records[0][2],
                  'url':records[0][3], 'twitter':records[0][4], 'facebook':records[0][5],
                  'youtube':records[0][6]}

  cursor.close()
  return jsonify(result)
#*********************************************************************************************************************
#INSERT FUNCTIONS AND END POINTS WITH NAMES HERE

#Ravi's query:
#Don't mind the caps locks, it should work as is
@app.route('/congress/legislator/<state_code>', methods=['GET'])
def get_legislators_by_state(state):
  query = '''
    SELECT 'HREP' AS LTYPE, STATE, FNAME, LNAME, CONCAT(DAY(BIRTHDAY), ' ', MONTHNAME(BIRTHDAY), ' ',
    YEAR(BIRTHDAY)) BIRTHDAY, URL, TWITTER, FACEBOOK, YOUTUBE
    FROM HREP
    WHERE STATE = %s
    UNION
    SELECT 'SENATOR', STATE STATE, FNAME, LNAME, CONCAT(DAY(BIRTHDAY), ' ', MONTHNAME(BIRTHDAY), ' ',
    YEAR(BIRTHDAY)) BIRTHDAY, URL, TWITTER, FACEBOOK, YOUTUBE
    FROM SENATOR
    WHERE STATE = %s
    ORDER BY LTYPE, LNAME ASC
  '''
  cursor = db.cursor()
  cursor.execute(query,(state,))
  records = cursor.fetchall()
  if len(records) == 0:
    abort(404)
  legislators = []
  for record in records:
    legislators.append({'state':record[0], 'fname':record[1], 'lname':record[2],
                  'birthday':record[3],
                  'url':record[4], 'twitter':record[5], 'facebook':record[6],
                  'youtube':record[7]})

  result = {'Legislators':legislators}
  cursor.close()
  return jsonify(result)

#Preetham's query:
@app.route('/congress/senator/<state_code>', methods=['GET'])
def get_senators_by_state(state_code):
    query = '''select state, fname, lname, concat(DAY(birthday),' ',MONTHNAME(birthday), ' ', YEAR(birthday)) birthday, url, twitter, facebook, youtube from SENATOR where state = %s'''
    cursor = db.cursor()
    cursor.execute(query,(state_code,))
    records = cursor.fetchall()
    if len(records) == 0:
        abort(404)
    senators = []
    for record in records:
      senators.append({'state':record[0], 'fname':record[1], 'lname':record[2],
                  'birthday':record[3],
                  'url':record[4], 'twitter':record[5], 'facebook':record[6],
                  'youtube':record[7]})

    result = {'senators':senators}
    cursor.close()
    return jsonify(result)
  
#Emily's query:
@app.route('/congress/hrep/<state_code>', methods=['GET'])
def get_hreps_by_state(state_code):
    query = '''
      select fname, lname, concat(DAY(birthday),' ',MONTHNAME(birthday), ' ', YEAR(birthday)) birthday, url, twitter, facebook, youtube
      from HREP
      where state = %s
    '''
    cursor = db.cursor()
    cursor.execute(query,(state_code))
    records = cursor.fetchall()
    if len(records) == 0:
      abort(404)
    hreps = []
    for record in records:
      hreps.append({'state':record[0], 'fname':record[1], 'lname':record[2],
                  'birthday':record[3],
                  'url':record[4], 'twitter':record[5], 'facebook':record[6],
                  'youtube':record[7], 'district':record[8]})

    result = {'Representatives':hreps}
    cursor.close()
    return jsonify(result)
  
#Caroline's query:
@app.route('/congress/hrep/party/<party>', methods=['GET'])
def get_hrep_by_party(party):
  query = '''
    select state, fname, lname, concat(DAY(birthday),' ',MONTHNAME(birthday), ' ',
    YEAR(birthday)) birthday, url, twitter, facebook, youtube
    from HREP
    where party = %s
    order by state
  '''
  cursor = db.cursor()
  cursor.execute(query,(party,))
  records = cursor.fetchall()
  if len(records) == 0:
    abort(404)
  hrep = []
  for record in records:
    hrep.append({'state':record[0], 'fname':record[1], 'lname':record[2],
                  'birthday':record[3],
                  'url':record[4], 'twitter':record[5], 'facebook':record[6],
                  'youtube':record[7]})

  result = {'Representatives':hrep}
  cursor.close()
  return jsonify(result)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='localhost',debug=True)
    db.close()
