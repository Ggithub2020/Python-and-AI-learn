import sqlite3

connection=sqlite3.connect("sms.db")
cursor=connection.cursor()
Create_table="""
create table Student(
    StudentId int PRIMARY KEY,
    FirstName varchar(50),
    LastName varchar(50),
    Gender Char(1)
)
"""
cursor.execute(Create_table)
connection.commit()
cursor.close()
insert_student="""
insert into Student(StudentId,FirstName,LastName, Gender)
values(1,'John','Doe','M') 
"""
cursor.execute(insert_student)
connection.commit()
cursor.close()
query="select * from Student"
cursor.execute(query)
results=cursor.fetchall()
for row in results:
    print(row)
cursor.close()