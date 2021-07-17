import sqlite3

database=sqlite3.connect("user_data")
cursor=database.cursor()
cursor.execute("select * from user_db")
data=cursor.fetchall()
print(data)