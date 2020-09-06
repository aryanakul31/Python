import mysql.connector

con=mysql.connector.connect(
    user = "root",
    password = "",
    host = "localhost",
    database = "python"
)
cursor = con.cursor()

query = cursor.execute("select * from newaccount")
results = cursor.fetchall()

print(results[0][0])
# print(results[1])