num1=12
num2=13
sum = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum)
num1 = 12
num2 = 13
difference = num1 - num2
print("The difference between", num1, "and", num2, "is:", difference)
num1 = 20
num2 = 13
diff =num1%num2
print("The division of", num1, "by", num2, "is:", diff)
num1=12
exp= num1**2
exp2=num1**3
print("The cube of", num1, "is:", exp2)
print("The square of", num1, "is:", exp)
nu1=13
nu1+=13
print("The value of nu1 after addition is:", nu1)
with input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))  
sum = num1 + num2
diff = num1 % num2
exp = num1 ** 2
exp2 = num1 ** 3
diff = num1 - num2
remainder = num1 % num2
print("The sum of", num1, "and", num2, "is:", sum)
print("The difference between", num1, "and", num2, "is:", diff) 
print("The square of", num1, "is:", exp)
print("The cube of", num1, "is:", exp2)

# or
print("Sum is " + str(sum))
print("Difference is " + str(diff))
print("Square is " + str(exp))
print("Cube is " + str(exp2))
print("Remainder when", num1, "is divided by", num2, "is:", remainder)
# or using f-strings
print(f"The sum of {num1} and {num2} is: {sum}")
print(f"The difference between {num1} and {num2} is: {diff}")
print(f"The square of {num1} is: {exp}")

#or
print(f"The sum is {num1} is: {exp2}")
print(f"The cube of {num1} is: {exp2}")
print(f"The remainder when {num1} is divided by {num2} is: {remainder}")
# or using format method
print("The sum of {} and {} is: {}".format(num1, num2, sum))
print("The difference between {} and {} is: {}".format(num1, num2, diff))
print("The square of {} is: {}".format(num1, exp))  