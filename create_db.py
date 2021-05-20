import sqlite3

con = sqlite3.connect("./db.db")
cur = con.cursor()
sql = """
CREATE TABLE IF NOT EXISTS phones (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, value VARCHAR(50));
"""

cur.execute(sql)

con.close()
