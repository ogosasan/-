import sqlite3
database = "iu4.db"
con = sqlite3.connect(database)

cur = con.cursor()
s = """CREATE TABLE Countries (
     ID INTEGER PRIMARY KEY AUTOINCREMENT,
     Country VARCHAR(30) NOT NULL,
     Capital VARCHAR(30) NOT NULL,
     Population INTEGER NOT NULL,
     Language VARCHAR(30) NOT NULL
 );"""
cur.execute(s)

con.close()

