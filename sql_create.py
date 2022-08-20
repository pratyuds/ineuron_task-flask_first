import mysql.connector as conn

mydb = conn.connect(host="localhost", user="root", password="Chahit@1117")
print(mydb)
cursor = mydb.cursor()
# cursor.execute("create database api_database")
# cursor.execute("show databases")
# q1 = cursor.execute(
#     "create table api_database.ineuron(emp_id int(10) ,emp_name varchar(80), emp_mailid varchar(20),emp_salary int(6), emp_attendence int(3))")
q2 = cursor.execute("select * from api_database.ineuron")
for i in cursor.fetchall():
    print(i)