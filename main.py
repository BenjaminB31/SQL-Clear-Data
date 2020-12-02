# coding: utf-8
import time
import mysql.connector

start = time.time()

mydb = mysql.connector.connect(
  host="HOST",
  user="USER",
  password="PASSWORD",
  database="DATABASE"
)

table = "TABLE"

# EXEMPLE
request = [
"Message = 'Donnee a supprimer'",
"Message like 'Donnee a supp%'",
]

value = " OR ".join(request)

mycursor = mydb.cursor()

sql = f"DELETE FROM {table} WHERE {' OR '.join(request)};"

mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "rows in set.")

mycursor.close()
mydb.close()

stop = time.time()
print("Execute time :", stop - start)