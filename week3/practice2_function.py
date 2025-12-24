#functions are block of code that only runs when it is called
def Add(num1, num2):
    return num1 + num2

print(Add(5, 3))  # Output: 8

def Subtract(num1, num2):
    return num1 - num2  
print(Subtract(5, 3))  # Output: 2

def Multiply(num1, num2):
    return num1 * num2
print(Multiply(5, 3))  # Output: 15
def Divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2
print(Divide(5, 3))  # Output: 1.6666666666666667
def Modulus(num1, num2):
    return num1 % num2
print(Modulus(5, 3))  # Output: 2
def Exponent(num1, num2):
    return num1 ** num2
print(Exponent(5, 3))  # Output: 125
def Floor_Division(num1, num2):
    return num1 // num2
print(Floor_Division(5, 3))  # Output: 1
def Absolute(num):
    return abs(num)
print(Absolute(-5))  # Output: 5
def Square_Root(num):
    if num < 0:
        return "Error: Cannot compute square root of a negative number."
    return num ** 0.5