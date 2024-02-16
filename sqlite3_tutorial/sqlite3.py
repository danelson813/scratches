import sqlite3

# conn = sqlite3.connect('my_databvase.db')

# cursor = conn.cursor()
# data_tulple = ('John', 28, 'New York', 50000)
# cursor.exrecute("INSERT INTO COMPANY (NAME, AGE, ADDRESS, SALARY) VALUES (?, ?, ?, ?)", data_tulple)


# more complete code:
conn = sqlite3.connect("my_database.db")
cur = conn.cursor()
cur.execute('''
    CREATE TABLE company(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        AGE INT NOT NULL,
        ADDRESS CHAR(50),
        SALARY REAL
);
''')

cursor = conn.cursor()
data_tulple = ('John', 28, 'New York', 50000)
cursor.exrecute("INSERT INTO COMPANY (NAME, AGE, ADDRESS, SALARY) VALUES (?, ?, ?, ?)", data_tulple)

# or

sql_insert = ("insert into company(NAME, AGE, ADDRESS, SALARY) VALUES ('Tom, 25, 'Edinburgh), 12000")
cursor.execute(sql_insert)

# selecting data from a table

def select_data(conn, sql):
    cur = conn.cursor()
    cur.exercute(sql)
    rows = cur.fetchall()
    print(rows)


sql = "select name, age, address,salary from company"
select_data(conn, sql)

# Using transactions:

import sqlite3

# Connect to the database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

try:
    # Start the transaction
    cursor.execute("BEGIN TRANSACTION;")
    
    # Insert some sample data into the COMPANY table
    cursor.execute("INSERT INTO company(NAME, AGE, ADDRESS, SALARY) VALUES ('James',34,'Dublin', 50000);")
    cursor.execute("INSERT INTO company(NAME, AGE, ADDRESS, SALARY) VALUES ('Anna', 22, 'Los Angeles', 45000);")
    # deliberate syntax error below
    cursor.execute("INSRT INTO company(NAME, AGE, ADDRESS, SALARY) VALUES ('Mike', 32, 'Chicago', 60000);")
    
    # Commit the transaction
    cursor.execute("COMMIT;")
    print("Data inserted successfully")

except sqlite3.Error as e:
    # Rollback the transaction in case of any errors
    cursor.execute("ROLLBACK;")
    print(f"Error: {e}")

finally:
    conn.close()


# When the above code runs it prints out the following:
#
# Error: near "INSRT": syntax error
#
#
# And because it's in a transaction it means none of 
# the records will be inserted into the table
#
    


#     Upserting data

# In SQLite, an “upsert” operation (a blend of “update” and “insert”) can be achieved using the INSERT ON CONFLICT clause.

# Here’s an example using a table called employee that has an ID column which is a unique identifier for records in the table. If a record with a given ID exists, we'll update its details; if it doesn't, we'll insert a new record.

# First, let’s insert our initial data.

# create the employee table and insert some initial data

import sqlite3

# Connect to the database
conn = sqlite3.connect('my_database.db')

c=conn.cursor()

c.execute('''
CREATE TABLE employee(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50),
    SALARY REAL
);
''')
conn.commit()

cursor.execute('''
INSERT INTO employee (ID, NAME, AGE, ADDRESS, SALARY) 
VALUES (1, 'John', 28, 'New York', 50000) 
''')
               

cursor.execute('''
INSERT INTO employee (ID, NAME, AGE, ADDRESS, SALARY) 
VALUES (2, 'Anna', 22, 'Los Angeles', 45000) 
''')

conn.commit()


sql="select * from employee"

select_data(conn,sql)


=>  

[
(1, 'John', 28, 'New York', 50000.0), 
(2, 'Anna', 22, 'Los Angeles', 45000.0)
]

'''
Now, let’s insert some more data. Two of the records will have the same ID as before but a different salary so we want that value to be updated in the table, and the other record will be a completely new record which should just be inserted into the table as normal.
'''

import sqlite3

# Connect to the database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Upsert data into the COMPANY table
cursor.execute('''
INSERT INTO employee (ID, NAME, AGE, ADDRESS, SALARY) 
VALUES (1, 'John', 28, 'New York', 36000) 
ON CONFLICT(ID) 
DO UPDATE SET NAME='John', AGE=28, ADDRESS='New York', SALARY=36000;
''')

cursor.execute('''
INSERT INTO employee (ID, NAME, AGE, ADDRESS, SALARY) 
VALUES (2, 'Anna', 22, 'Los Angeles', 19000) 
ON CONFLICT(ID) 
DO UPDATE SET NAME='Anna', AGE=22, ADDRESS='Los Angeles', SALARY=19000;
''')

cursor.execute('''
INSERT INTO employee (ID, NAME, AGE, ADDRESS, SALARY) 
VALUES (3, 'Tom', 28, 'Edinburgh', 45000) 
ON CONFLICT(ID) 
DO UPDATE SET NAME='Tom', AGE=28, ADDRESS='Edinburgh', SALARY=45000;
''')

conn.commit()

sql="select * from employee"

select_data(conn,sql)


=> 
[
(1, 'John', 28, 'New York', 36000.0), 
(2, 'Anna', 22, 'Los Angeles', 19000.0), 
(3, 'Tom', 28, 'Edinburgh', 45000.0)
]