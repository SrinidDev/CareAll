import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="Careall")

mycursor = mydb.cursor()
#Let the Young chap be: bbb
mycursor.execute("SELECT Ename FROM Elder WHERE Elder.Eid in(SELECT Eid FROM YCaresE WHERE Yid in (SELECT Yid FROM Youth WHERE Yname='bbb'))");

for i in mycursor:
    print(i)
