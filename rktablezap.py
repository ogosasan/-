import sqlite3

database = "iu4.db"

con = sqlite3.connect(database)
cur = con.cursor()

s = """INSERT INTO Countries VALUES (1, 'Россия', 'Москва', '2000000000', 'Русский')"""
cur.execute(s)
s = """INSERT INTO Countries(Country, Capital, Population, Language)
VALUES ('США', 'Нью Йорк', '150000000', 'Английский')"""
cur.execute(s)
con.commit()
con.close()
