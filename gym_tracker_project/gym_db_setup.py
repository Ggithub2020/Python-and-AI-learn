
import pyodbc

server = 'DEA2025\GMSSQLSERVER_DEV'

# Connect WITHOUT specifying a database
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    f'SERVER={server};'
    'Trusted_Connection=yes;',
    autocommit=True  # IMPORTANT: must be True for CREATE DATABASE
)

cursor = conn.cursor()

# Create database if it doesn't exist
cursor.execute("IF DB_ID('GymDB') IS NULL CREATE DATABASE GymDB;")

print("Database created successfully!")

# Close connection
conn.close()

