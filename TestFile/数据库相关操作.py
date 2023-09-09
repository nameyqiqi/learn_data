import mysql.connector
import MySQLdb
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database='trip_db'
)
mycursor = mydb.cursor()
mycursor.execute("truncate table trip")
for x in mycursor:
    print(x,type(x))
#创建table
# sql_create="CREATE TABLE sites(name VARCHAR(25),url VARCHAR(255))"
# mycursor.execute(sql_create)
#
# # #插入数据
# sql_insert = "INSERT INTO sites (name, url) VALUES (%s, %s)"
# val = ("Zhihu", "https://www.zhihu.com")
# mycursor.execute(sql_insert, val)
#
# #删除表 谨慎使用
# sql_delete="DROP TABLE sites"
# mycursor.execute(sql_delete)

#更新数据表
# sql_update="update sites "
# try:
#     mycursor.execute(sql_create)#创建表
#     mycursor.execute(sql_insert, val)#插入数据
#     mycursor.execute(sql_delete)#删除表 慎用
#     #执行数据库操作
#     mydb.commit()
# except:
#     #发生错误回滚
#     mydb.rollback()
# mydb.close()


