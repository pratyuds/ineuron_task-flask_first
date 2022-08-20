import pymongo
from flask import Flask, request, jsonify

app =Flask(__name__)

@app.route('/mongo_fetch',methods = ['GET' ,'POST'])
def fetch_mongo():
    if(request.method=='POST'):
        emp_id = request.json['id']
        emp_name = request.json['name']
        emp_mail = request.json['email']
        sal = request.json['salary']
        attend = request.json['attendence']


        client = pymongo.MongoClient("mongodb+srv://ineuron_pratyu:Chahit1117@pratyusha.dc3s9sa.mongodb.net/?retryWrites=true&w=majority")
        db = client.test

        print(db)

        d = {
            "emp_id" : emp_id,
            "emp_name" : f"'{emp_name}'",
            "emp_mail" : f"'{emp_mail}'",
            "emp_salary" : sal,
            "emp_attendence": attend
        }


        db1 = client['mongo_flask']
        col1 = db1['flask_test']
        record = col1.find({"$and" : [{'emp_id': emp_id},{'emp_name': f"'{emp_name}'"},{'emp_mail': f"'{emp_mail}'"},{'emp_salary': sal}]})  #fetch operation
        print(record)
        for i in record:
            return jsonify((str(i)))

if __name__ =='__main__' :
    app.run()
