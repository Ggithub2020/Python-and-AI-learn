fName ="Girum "
mName = "Legese"
lName = "Obse"
#print(fName + lName) # Concatenation
print(fName + " " + lName) # Concatenation with space
print(fName*10) # Repetition
print(fName + " " + lName + " is a software engineer") # Concatenation with space and additional text
content ="To__________________________________________\n" +"You are invited to the party\n" + "at my house on Saturday\n" + "at 6:00 PM"
print(content*10) # Repetition of the invitation content
print("To " + fName + " " + lName + "\nYou are invited to the party\nat my house on Saturday\nat 6:00 PM") # Formatted invitation

#print Girum L.Obse
print(fName + ""+ mName[0:1] + "." + lName)
print(fName + ""+ mName[0:2] + "." + lName)
print(fName + ""+ mName[0:3] + "." + lName)

print(fName.upper() + " " + lName.upper()) # Uppercase first and last name
print(fName.lower() + " " + lName.lower()) # Lowercase first and last name
titles = "Software Engineer, Data Scientist, Web Developer"
print(titles.split(", ")) # Split titles by comma and space
print(titles.split(", ")) # Split titles by comma and space
print(titles.split(", ")[0]) # Get the first title
print(titles.title()) # Get the second title
titles = "please, do not use this title and use the one above"
print(titles.title()) # Capitalize the first letter of each word in the string
print(titles.capitalize()) # Capitalize the first letter of the string