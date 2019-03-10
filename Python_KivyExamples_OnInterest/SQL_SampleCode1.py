import sqlite3

user_FirstName = '?'
user_LastName = '?'
user_JobCurrent = '?'

conn = sqlite3.connect('EXI_SMV_AppData.db')
#cursor = conn.execute("SELECT * FROM user_TableDatabase")
cursor = conn.execute('SELECT * FROM user_TableDatabase')
rows = cursor.fetchall()

for row in rows:
    print (row)