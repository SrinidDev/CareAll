import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="Careall")

mycursor = mydb.cursor()
mycursor.execute("SELECT Yname,Ename FROM Youth,Elder,YCaresE WHERE Youth.Yid=YCaresE.Yid AND Elder.Eid=YCaresE.Eid;")
for i in mycursor:
    print(i)
