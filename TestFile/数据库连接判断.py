import MySQLdb
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="trip_db"
)
mycursor = db.cursor()
sql_insert = "INSERT INTO trip (name, adress,mark,remark_on,reamke_it) VALUES (%s,%s,%s,%s,%s)"
value=('1','2','3','4','5')
mycursor.execute(sql_insert,value)
db.commit()
db.close()
# print(mycursor.execute("SHOW DATABASES like'akdc'"))
# mycursor.execute("CREATE DATABASE trip_db")
# result = mycursor.execute("SHOW DATABASES like'trip_db'")
# if result <= 0:
#     mycursor.execute("CREATE DATABASE 'trip_db'")
#     mycursor.execute("CREATE TABLE trip (name VARCHAR(25), adress VARCHAR(50),"
#                      "mark VARCHAR(10),remark_on VARCHAR(1500),reamke_it VARCHAR(25) )")
