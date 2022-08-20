import mysql.connector as conn
from flask import Flask, request, jsonify

app =Flask(__name__)

@app.route('/fetch',methods = ['GET' ,'POST'])
def fetch_new():
    if(request.method=='POST'):
        emp_id = request.json['id']
        emp_name = request.json['name']
        emp_mail = request.json['email']
        sal = request.json['salary']
        attend = request.json['attendence']
        mydb = conn.connect(host="localhost", user="root", password="Chahit@1117")
        cursor = mydb.cursor()
        s = f"select * from api_database.ineuron where emp_id like {emp_id} and emp_name like '{emp_name}' and emp_mailid like '{emp_mail}' and emp_salary like {sal} and emp_attendence like {attend}"

        cursor.execute(s)

        record = cursor.fetchall()

        mydb.commit()

        for i in record:
            return jsonify((i))


if __name__ =='__main__' :
    app.run()
