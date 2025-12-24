# # entry1=int(input("Enter your first number: "))
# # entry2=int(input("Enter your second number: "))
# # x = entry1 + entry2
# # sum = x
# # y =  entry1 - entry2
# # diff = y
# # z= entry1 * entry2
# # prod = z
# # r= entry1 / entry2
# # quot = r
# # k= entry1 % entry2
# # rem = k
# # q= entry1 ** entry2
# # power = q

# # print("The sum of ",entry1,"and",entry2,"is",sum)
# # print("The difference when",entry2,"is subtracted from",entry1,"is",diff)
# # print("The product of",entry1,"and",entry2,"is",prod)
# # print("The quotient when",entry1,"is divided by",entry2,"is",quot)
# # print("The remainder when",entry1,"is divided by",entry2,"is",rem)
# # print(entry1,"raised to the power of",entry2,"is",power)
# # # This program takes two numbers as input and performs basic arithmetic operations on them.

# # entry1=str(input("enter your first name: "))
# # entry2=str(input("enter your last name: ")) 
# # date_of_birth=str(input("enter year of birth: "))
# # enter_place=str(input("enter your place of birth: "))
# # enter_adress=str(input("enter your address: "))
# # full_name = entry1 + " " + entry2
# # age = 2025 - int(date_of_birth.split("-")[0])  # Assuming date_of_birth is in YYYY-MM-DD format
# # summary = f"your full name is: {full_name}\nAge: {age}\nPlace of Birth: {enter_place}\nAddress: {enter_adress} and thanks for using our services and please visit again and for any question please visit website www.xyz.com"
# # print(summary)
# # This program collects personal information from the user and displays a summary.
# # states=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia",
# # "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
# # "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
# # "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
# # "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
# # cities={"Alabama":"Montgomery", "Alaska":"Juneau", "Arizona":"Phoenix", "Arkansas":"Little Rock", "California":"Sacramento",
# # "Colorado":"Denver", "Connecticut":"Hartford", "Delaware":"Dover", "Florida":"Tallahassee", "Georgia":"Atlanta",
# # "Hawaii":"Honolulu", "Idaho":"Boise", "Illinois":"Springfield", "Indiana":"Indianapolis", "Iowa":"Des Moines", "Kansas":"Topeka", "Kentucky":"Frankfort", "Louisiana":"Baton Rouge",}
# # print("List of US States:")
# # print(states)
# # print("Total number of states:", len(states))
# # print(states[20])
# # print("Capital Cities of some States:")
# # for state, capital in cities.items():
# #     print(f"The capital of {state} is {capital}.")
# # vegies = {"carrot", "broccoli", "spinach", "potato", "onion"}
# # fruits = {"apple", "banana", "orange", "grape", "mango"}
# # n=vegies.union(fruits)
# # print("Union of vegetables and fruits:", n)
# for i in range(2,40): # 0 1 2 3
#     for j in range(1, 30): # 1, 2, 3, 4, 5  
#         print(j, end=" ") #
#     print()

num = 1
for i in range(1, 45):
    for j in range(i):
        print(num, end=" ")
        num += 5
    print()
