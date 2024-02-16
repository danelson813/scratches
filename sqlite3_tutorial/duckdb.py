# pip install duckdb==0.9.1


# Creating tables
'''
import duckdb

duckdb.sql("CREATE TABLE t1(id INTEGER PRIMARY KEY, j VARCHAR)")
results =duckdb.sql("select * from t1")
results



┌───────┬─────────┐
│  id   │    j    │
│ int32 │ varchar │
├─────────────────┤
│     0 rows      │
└─────────────────┘
'''

'''
Populating tables

duckdb.sql("insert into t1(id,j) values(1,2)")
results =duckdb.sql("select * from t1")
results


┌───────┬─────────┐
│  id   │    j    │
│ int32 │ varchar │
├───────┼─────────┤
│     1 │ 2       │
└───────┴─────────┘'''


'''
One huge advantage DuckDB has is that you can also populate tables with data from Pandas, Polars and Vaex dataframes. Here’s a Pandas example.

import duckdb
import pandas

# Create a Pandas dataframe
my_df = pandas.DataFrame.from_dict({'a': [1,2,3,4,5,6,7,8,9]})

# create the table "my_table" from the DataFrame "my_df"
# Note: duckdb.sql connects to the default in-memory database connection
duckdb.sql("CREATE TABLE my_table AS SELECT * FROM my_df")

results =duckdb.sql("select * from my_table")
results

┌───────┐
│   a   │
│ int64 │
├───────┤
│     1 │
│     2 │
│     3 │
│     4 │
│     5 │
│     6 │
│     7 │
│     8 │
│     9 │
└───────┘


#
# You can also insert into an existing table from a dataframe
#
my_df = pandas.DataFrame.from_dict({'a': [99,100,101,102,103]})
duckdb.sql("INSERT INTO my_table SELECT * FROM my_df")
results =duckdb.sql("select * from my_table")
results

┌───────┐
│   a   │
│ int64 │
├───────┤
│     1 │
│     2 │
│     3 │
│     4 │
│     5 │
│     6 │
│     7 │
│     8 │
│     9 │
│    99 │
│   100 │
│   101 │
│   102 │
│   103 │
└───────┘
'''


'''
Deleting data

duckdb.sql("delete from my_table where a in (1,2,3,4,5)")
results =duckdb.sql("select * from my_table")
results

┌───────┐
│   a   │
│ int64 │
├───────┤
│     6 │
│     7 │
│     8 │
│     9 │
│    99 │
│   100 │
│   101 │
│   102 │
│   103 │
└───────┘
'''


'''
Upserting table data

As well as a regular SQL update command (which I won’t show), DuckDB also provides an upsert mechanism. To do this there is an unusual INSERT OR REPLACE SQL command. Here’s how it works.

import duckdb
duckdb.sql("CREATE TABLE t1(id INTEGER PRIMARY KEY, j VARCHAR)")

# populate table t1 with some initial data

duckdb.sql("INSERT OR REPLACE INTO t1(id,j) VALUES(1,2)")
duckdb.sql("INSERT OR REPLACE INTO t1(id,j) VALUES(3,4)")

results =duckdb.sql("select * from t1")
results

┌───────┬─────────┐
│  id   │    j    │
│ int32 │ varchar │
├───────┼─────────┤
│     1 │ 2       │
│     3 │ 4       │
└───────┴─────────┘

# Now see what happens if we try to insert the 
# same 'id' value with a different 'j' value

duckdb.sql("INSERT OR REPLACE INTO t1(id,j) VALUES(1,99)")
duckdb.sql("INSERT OR REPLACE INTO t1(id,j) VALUES(3,42)")
results =duckdb.sql("select * from t1")
results

┌───────┬─────────┐
│  id   │    j    │
│ int32 │ varchar │
├───────┼─────────┤
│     1 │ 99      │
│     3 │ 42      │
└───────┴─────────┘
'''


'''
Using persistent storage
By default, DuckDB operates on an in-memory database. That means that any tables created are not persisted to disk, and when you end your Python or Jupyter Notebook session, that data is gone. If you don’t want that to happen, you can persist your data to disk using the connect method. Any data written using that connection will be saved and can be reloaded by re-connecting to the same file. For example,

import duckdb
# create a connection to a file called 'file.db'
con = duckdb.connect('file.db')
# create a table and load data into it
con.sql('CREATE TABLE test(i INTEGER)')
con.sql('INSERT INTO test VALUES (42)')
# query the table
con.table('test').show()
# explicitly close the connection
con.close()

# If connecting again to file.db, your data will still be there

con = duckdb.connect('file.db')
con.sql("show all tables")


┌──────────┬─────────┬─────────┬──────────────┬──────────────┬───────────┐
│ database │ schema  │  name   │ column_names │ column_types │ temporary │
│ varchar  │ varchar │ varchar │  varchar[]   │  varchar[]   │  boolean  │
├──────────┼─────────┼─────────┼──────────────┼──────────────┼───────────┤
│ file     │ main    │ test    │ [i]          │ [INTEGER]    │ false     │
└──────────┴─────────┴─────────┴──────────────┴──────────────┴───────────┘

'''