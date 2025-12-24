import pyodbc
# print(pyodbc.drivers())
connection = pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=DEA2025\GMSSQLSERVER_DEV;'
    'Database=Gold_Business;'
    'Trusted_Connection=yes;' # Use this line for Windows Authentication
    'Encrypt=yes;'
    'TrustServerCertificate=yes;'
)
cursor= connection.cursor()
query = "select * from DimStates"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)
    
cursor.close()
connection.close()