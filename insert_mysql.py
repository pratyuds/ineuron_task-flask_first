import mysql.connector as conn
from flask import Flask, request, jsonify
import json
import collections

app =Flask(__name__)

@app.route('/insert',methods = ['GET' ,'POST'])
def insert_new():
    if(request.method=='POST'):
        emp_id = request.json['id']
        emp_name = request.json['name']
        emp_mail = request.json['email']
        sal = request.json['salary']
        attend = request.json['attendence']
        mydb = conn.connect(host="localhost", user="root", password="Chahit@1117")
        cursor = mydb.cursor()
        s = f"insert into api_database.ineuron values({emp_id},'{emp_name}','{emp_mail}',{sal},{attend})"
        s = cursor.execute(s)

        mydb.commit()

        cursor.execute("select * from pratyusha.ineuron")



        return jsonify(data=cursor.fetchall())



if __name__ =='__main__' :
    app.run()
