# list and tuple
# list
# my_youtube_videos=["powerBI", "Tableau", "SQL", "Python", "Excel", "R", "Java", "C++", "JavaScript", "Swift"]
# print(my_youtube_videos)
# print(my_youtube_videos[0])
# print(my_youtube_videos[1])
# print(my_youtube_videos[2])
# print(my_youtube_videos[3])
# print(my_youtube_videos[4])
# print(my_youtube_videos[5])
# print(my_youtube_videos[6])
# #how to replace an item in a list
# my_youtube_videos[1]="Power App"
# my_youtube_videos[2]="SQL Server"
# my_youtube_videos[3]="Python Programming"
# print(my_youtube_videos)
# print(my_youtube_videos[1])
# print(my_youtube_videos[2]) 
# print(my_youtube_videos[3])
# print(my_youtube_videos[4])
# print(my_youtube_videos[5])
# print(my_youtube_videos[6])

#example of a tuple
# my_youtube_videos_tuple=("PowerBI", "Tableau", "SQL", "Python", "Excel", "R", "Java", "C++", "JavaScript", "Swift")
# print(my_youtube_videos_tuple)
# print(my_youtube_videos_tuple[0])
# print(my_youtube_videos_tuple[1])
# print(my_youtube_videos_tuple[2])
# print(my_youtube_videos_tuple[3])
# print(my_youtube_videos_tuple[4])
# print(my_youtube_videos_tuple[5])
# print(my_youtube_videos_tuple[6])

#practice with input parameters arthimetic
# set1 = int(input("Enter the first number: "))
# set2 = int(input("Enter the second number: "))
# set3 = int(input("Enter the third number: "))
# print("The sum of the two numbers is: ", set1 + set2)
# print("The difference of the two numbers is: ", set1 - set2)
# print("The product of the two numbers is: ", set1 * set2)
#practice with filling formats and then print out summary
fname = input("Enter your name: ")
lname = input("Enter your last name: ")
fullname = fname + " " + lname
age = input("Enter your age: ")
city = input("Enter your city: ")
address = input("Enter your address: ")
country = input("Enter your country: ")
education = input("Enter your education: ")
experiance = input("Enter your experience: ")
company_previous = input("Enter your previous company: ")
Fulladress = address + " " + city + " " + country
skills = input("Enter your skills: ")
#print summary of the candidate in professional format in a short paragraph

professional_summary = "Thanks for Submitting the forms and here is the detail:" + "Full Name: " + fullname + " Age: " + age + " Address: " + Fulladress + " Education: "+ education + " Experience: " + experiance + " Previous Company: "+ company_previous + " Skills: " + skills
print("Professional Summary: ", professional_summary)
