# db1-1.py
import sqlite3

con = sqlite3.connect('test.db')
cur = con.cursor()

cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)
cur.close()