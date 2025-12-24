import pyodbc

connection = pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=DEA2025\GMSSQLSERVER_DEV;'
    'Database=AdventureWorksDW2022;'
    'Trusted_Connection=yes;' # Use this line for Windows Authentication
    'Encrypt=yes;'
    'TrustServerCertificate=yes;'
)
cursor= connection.cursor()
query = "SELECT TOP (100) CustomerID  ,NameStyle,Title,FirstName ,MiddleName ,LastName ,Suffix ,CompanyName ,SalesPerson,EmailAddress ,Phone  FROM AdventureWorksLT2012.SalesLT.Customer"
     
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)
    
cursor.close()
connection.close()


