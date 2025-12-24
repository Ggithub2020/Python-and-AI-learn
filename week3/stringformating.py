fNname = "Girum "
lName = "Legese"
tri ="Hello "+ fNname + " " + lName + "you are invited to the party at my house on Saturday at 6:00 PM"
print(tri)  # Concatenation of strings
print(f"Hello {fNname} {lName} you are invited to the party at my house on Saturday at 6:00 PM")  # f-string formatting----best practice
print("Hello {} {} you are invited to the party at my house on Saturday at 6:00 PM".format(fNname, lName))  # format method---not recommended
print("Hello {0} {1} you are invited to the party at my house on Saturday at 6:00 PM".format(fNname, lName))  # format method with positional arguments
print("Hello {fN} {l} you are invited to the party at my house on Saturday at 6:00 PM".format(fN=fNname, l=lName))  # format method with named arguments