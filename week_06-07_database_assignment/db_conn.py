import pyodbc

conn = pyodbc.connect(
    'DRIVER=ODBC Driver 17 for SQL Server;'
    'SERVER=sqllab.academic.walshcollege.edu;'
    'DATABASE=it412_class;'
    'UID=it412_sbrohl2;'
    'PWD=********'
    )

cursor = conn.cursor()

cursor.execute("select * from dbo.Names")
for row in cursor.fetchall():
    print(row)
