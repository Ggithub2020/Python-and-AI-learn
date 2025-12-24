# This code generates a wedding invitation card using string concatenation and prints it multiple times.

fName ="Girum"
lName = "Tadesse"
invitation_card= "Hello" + fName + " " + lName + ",\n" + \
    "You are kindly invited to our wedding ceremony.\n" + \
    "Date: _______________\n" + \
    "Time: _______________\n" + \
    "Venue: _______________\n" + \
    "Please join us in celebrating this special day!\n"
print(invitation_card * 5)  # Print the invitation card 10 times

# #again another invitation card

fName ="Girum"
mName = "Mekonnen"
lName ="Tadesse"
print((f"Hello {fName} {mName} {lName},\n"
    "You are kindly invited to our wedding ceremony.\n"
    "Date: _______________\n"
    "Time: _______________\n"
    "Venue: _______________\n"
    "Please join us in celebrating this special day!\n") * 5)  # Print the invitation card 10 times

coffee = "Coffee"
tea = "Tea" 

print(f"Hello, would you like some {coffee} or {tea}?")  # Using f-string for string formatting
print("Hello, would you like some {} or {}?".format(coffee, tea))  # Using format method for string formatting  
print("Hello, would you like some %s or %s?" % (coffee, tea))  # Using old-style string formatting
print("Hello, would you like some " + coffee + " or " + tea + "?")  # Using string concatenation
print("Hello, would you like some {0} or {1}?".format(coffee, tea))  # Using format method with positional arguments
print("Hello, would you like some {tea} or {coffee}?".format(coffee=coffee, tea=tea))  # Using format method with named arguments
print("Hello, would you like some {0} or {1}?".format(tea, coffee))  # Using format method with positional arguments in reverse order


# Real-World Example: Food Ordering Assistant
# python
# Copy
# Edit
# User choices
name = "Sara"
main_dish = "burger"
side = "fries"
drink = "lemonade"
delivery_time = 30  # in minutes
total_price = 12.75
is_contactless = True

# # Message generation
print(f"Hi {name}, thanks for your order!")

print(f"You’ve ordered a {main_dish} with {side} and a glass of {drink}.")
print(f"Your total comes to ${total_price:.2f}.")

if is_contactless:
    print("We’ll deliver your order contactlessly to your doorstep.")
else:
    print("Your order will be handed to you in person.")

print(f"Estimated delivery time: {delivery_time} minutes.")


# Items bought
item1 = "Sandwich"
price1 = 5.50

item2 = "Coffee"
price2 = 3.00

item3 = "Cookie"
price3 = 2.25

# Calculate total
subtotal = price1 + price2 + price3
tax_rate = 0.07  # 7% tax
tax = subtotal * tax_rate
total = subtotal + tax

# Print receipt
print("===== Cafe Receipt =====")
print(f"{item1:15} ${price1:.2f}")
print(f"{item2:15} ${price2:.2f}")
print(f"{item3:15} ${price3:.2f}")
print("------------------------")
print(f"{'Subtotal':15} ${subtotal:.2f}")
print(f"{'Tax (7%)':15} ${tax:.2f}")
print(f"{'Total':15} ${total:.2f}")
print("========================")
print("Thank you for visiting!")




# Customer info
client_name = "John Doe"
company = "TechFix Solutions"

# Services provided
service1 = "Virus Removal"
price1 = 80.00

service2 = "Software Installation"
price2 = 50.00

service3 = "System Cleanup"
price3 = 40.00

# Totals
subtotal = price1 + price2 + price3
tax_rate = 0.10  # 10% service tax
tax = subtotal * tax_rate
total = subtotal + tax

# Print IT service receipt
print(f"===== {company} - Service Invoice =====")
print(f"Client: {client_name}")
print("----------------------------------------")
print(f"{service1:25} ${price1:.2f}")
print(f"{service2:25} ${price2:.2f}")
print(f"{service3:25} ${price3:.2f}")
print("----------------------------------------")
print(f"{'Subtotal':25} ${subtotal:.2f}")
print(f"{'Service Tax (10%)':25} ${tax:.2f}")
print(f"{'Total Amount':25} ${total:.2f}")
print("========================================")
print("Thank you for choosing TechFix Solutions!")
