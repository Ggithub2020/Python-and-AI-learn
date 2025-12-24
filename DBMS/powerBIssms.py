import pyodbc
# print(pyodbc.drivers())
connection = pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=rhd2z6dfhucexgphvprqc5esrm-o5ys57ihywzundt6qoeqcucj5q.database.fabric.microsoft.com,1433;'
    'Database=test-5b5f42c0-9afb-486d-b3ea-17b10c8be475;'
    'Trusted_Connection=yes;' # Use this line for Windows Authentication
    'Encrypt=yes;'
    'TrustServerCertificate=yes;'
)
cursor= connection.cursor()
query = "select * from TableName"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)
    
cursor.close()
connection.close()