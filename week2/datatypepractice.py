# num1 = 10
# num2 = 13

# sum = num1 + num2
# print(sum)
# division = num1 / num2
# print(division)
# multiplication = num1 * num2
# print(multiplication)
# print(type(num1))
# print(type(num2))
# print(type(sum))
# print(type(division))

# first_name ="Abebech"
# last_name = "Tadesse"   
# email = "test1@gmail.com"
# print(type(first_name))
# print(type(last_name))  
# print(type(email))
# print(type(first_name + last_name))
# print(first_name + last_name + email)
# payment_status = True
# payment_status = False
# print(type(payment_status))
# #List
# fruit =["apple", "banana", "cherry", "orange", "kiwi", "mango", "grape", "pear", "peach", "plum"]
# print(fruit[0])
# print(fruit[0])
# print(fruit[1])
# print(fruit[2])
# fruit[1] = "Avocado"
# for f in fruit:
    # print(f)
# print(type(fruit[1]))
# print(type(fruit[2]))       
# print(fruit[5])
# fruit [1] = "strawberry"
# fruit[5] = "blueberry"
# for f in fruit:
#     print(f)

# students = ["John", "Jane", "Doe"]
# print(students[0])
# print(students[1])  
# print(students[2])

# Tuple
# months =("January", "Feburary", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

# print(months[0])
# print(months[1])
# print(months[2])
# print(months[3])
# print(months[4])
# print(months[5])
# print(months[6])
# print(months[7])
# print(months[8])
# print(months[9])
# print(months[10])
# print(months[11])   
# # for m in months:
# # print(type(months))
#tuple
# months = ("January", "Feburary", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
# print(months[0])
# print(months[1  ])
# print(months[2])
# print(months[3])    
# print(months[4])
# print(months[5])
# print(months[6])
# print(months[7])
# print(months[8])
# print(months[9])
# print(months[10])
# print(months[11])

#set
# set_of_names = {"John", "Doe", "Jane", "Doe", "John", "Jane", "Doe"}  # Set automatically removes duplicates
# for name in set_of_names:
#     print(name)
#dictionary
# students = { "name": "Abebe", "age":43,"email": "abebe.feleke@test.com"}
# print(students["name"])
# print(students["age"])
# print(students["email"])
# print(type(students))


# students = [
#   {"name": "John", "age": 20, },
#   {"name": "Jane", "age": 22, },
#   {"name": "Doe", "age": 21, }, 
#   {"name": "Abebe", "age": 43,}
#  ]
            
                 
# for student in students:
#     for key, value in student.items():
#         print(f"{key}: {value}")
#         print(type(student))
#List []
# students = ["John", "Jane", "Doe"]
# students.append("Abebe")
# students.append("Tadesse")
# students.append("Feleke")
# students.append("Tesfaye")
# students.append("Tesfaye")
# print(students)
# students.remove("Tesfaye")
# print(students)
# students.insert(0, "Jemal")
# print(students)
# students.sort()
# print.reverse(students)
# set = {10, 20, 30, 40, 50,20, 30, 40, 50, 10}
# print(set)
# set.add(60)
# for n in set:
#     print(n)    
# set.remove(20)
# print(set)
# for n in set:
#     print(n)    

# number1={1,2,3,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10,10}  # Set automatically removes duplicates

# number2={11,12,13,14,15,16,17,18,19,20}
# # union_set = number1.union(number2)    
# nu= number1.union(number2)
# print(nu)
# for n in nu:
#     print(n)
# ni = number1.intersection(number2)
# print(ni)
# for n in ni:
#     print(n)
# nd = number1.difference(number2)
# print(nd)
students = {"fName": "Abebe", "lName": "Tadesse", "gender": "M", "age": 43, "email": "abebe@yahoo.com"} 
print(students.get("fName"))
print(students.get("lName"))    
print(students.get("gender"))
print(students.get("age"))