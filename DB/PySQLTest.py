import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  auth_plugin='mysql_native_password',
  database='project'
)

print(mydb)

mycursor = mydb.cursor()

word=input("Enter Word :")
count=input ("Enter Count :")

sql = "INSERT INTO project (word, count) VALUES (%s, %s)"
val = (word,count)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
