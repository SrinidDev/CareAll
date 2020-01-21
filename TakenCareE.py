import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="EdYoda")

mycursor = mydb.cursor()
mycursor.execute("SELECT Ename FROM Elder WHERE Elder.Eid in(SELECT Eid FROM YCaresE WHERE Yid in (SELECT Yid FROM Youth WHERE Yname='bbb'))");

for i in mycursor:
    print(i)
