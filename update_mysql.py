import mysql.connector as conn
from flask import Flask, request, jsonify

app =Flask(__name__)

@app.route('/update',methods = ['GET' ,'POST'])
def update_new():
    if(request.method=='POST'):
        emp_id = request.json['id']
        emp_name = request.json['name']
        emp_mail = request.json['email']
        sal = request.json['salary']
        attend = request.json['attendence']
        mydb = conn.connect(host="localhost", user="root", password="Chahit@1117")
        cursor = mydb.cursor()
        s = f"update api_database.ineuron set emp_id = {emp_id},emp_name ='{emp_name}',emp_mailid = '{emp_mail}',emp_salary={sal},emp_attendence = {attend} where emp_id = {emp_id}"
        s = cursor.execute(s)

        mydb.commit()

        cursor.execute("select * from pratyusha.ineuron")
        l = []
        for i in cursor.fetchall():
            l.append(i)
        return jsonify((l))

if __name__ =='__main__' :
    app.run()
