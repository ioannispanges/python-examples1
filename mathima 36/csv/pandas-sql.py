import sqlite3
import pandas as pd

conn = sqlite3.connect(':memory:')

create_table_query = '''
CREATE TABLE students (
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER,
grade TEXT
);
'''
conn.execute(create_table_query)

sample_data = [
    (1, 'Alice', 25, 'A'),
    (2, 'Bob', 30, 'B'),
    (3, 'Charlie', 22, 'C')
]

insert_data_query = 'INSERT INTO students(id,name, age,grade) VALUES (?,?,?,?);'
conn.executemany(insert_data_query, sample_data)

sql_query = 'SELECT * FROM students'
df_sql = pd.read_sql(sql_query, conn)

conn.close()

print("\nSQL Data:")
print(df_sql)
