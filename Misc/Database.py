import sqlite3

def createtable():
    conn=sqlite3.connect('lite.db')
    cur=conn.cursor()
    conn.execute("CREATE TABLE data(rollno INTEGER, name TEXT, marks REAL) ")
    conn.commit()
    conn.close()

createtable()