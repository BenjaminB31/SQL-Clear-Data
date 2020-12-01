import time
tps1 = time.time()
import mysql.connector

mydb = mysql.connector.connect(
  host="HOST",
  user="USER",
  password="PASSWORD",
  database="DATABASE"
)

table = "TABLE"

request = []

# EXEMPLE
request.append("Message = 'Donnee a supprimer'")
request.append("Message like 'Donnee a supp%'")



for i in request:
        if request.index(i) < 1 :
                value = request[0]
        else:
                value = str(value) + " OR " + str(i)


mycursor = mydb.cursor()

sql = "Delete from " + str(table) + " where " + str(value) + ";"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "rows in set.")

mycursor.close()
mydb.close()

tps2 = time.time()
print("Execute time :", tps2 - tps1)