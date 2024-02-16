# sqlite3_snippet.py
import sqlite3


# create a connection
conn = sqlite3.connect('db_name.db')
c = conn.cursor()   # cursor

# create a table
c.execute("""
    CREATE TABLE tablename(
    name TEXT,
    age INTEGER,
    height REAL
    )
""")

# insert data into a table
c.execute("INSERT INTO tablename VALUES ('mark', 20, 1.9)")

all_students = [
    ('john', 21, 1.8),
    ('david', 35, 1.7)
    ('michael', 19, 1.83),
]

c.executemany("INSERT INTO tablename VALUES (?, ?, ?)", all_students)

# select data
c.execute("SELECT * FROM tablename")
print(c.fetchall())

# commit
conn.commit()

# close the connection
conn.close()
