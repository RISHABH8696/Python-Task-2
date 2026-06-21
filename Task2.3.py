# Task-2: Python Decision Making & Functions

# Task 2.3: Practice Coding

# "Project 1: Grade Calculator Based on Marks"

# Requirements
#    Accept marks as input
#    Calculate grade using conditions
#    Display grade

# Sample Output
#     Enter Marks: 88
#     Grade: A

marks = int(input("Enter Marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "C"

print("Grade:", grade)

# Project 2: Temperature Converter (Celsius to Fahrenheit)

# Formula
# F=(C\\times\\frac{9}{5})+32

# Sample Output
#     Enter Temperature: 25
#     Temperature in Fahrenheit: 77.0°F

celsius = float(input("Enter Temperature: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

# Project 3: Simple Login Validation

# Requirements
#    Store username and password
#    Validate user input
#    Show success or failure message

# Sample Output
#     Username: admin
#     Password: 1234
#     Login Successful

username = "admin"
password = "1234"

u = input("Username: ")
p = input("Password: ")

if u == username and p == password:
    print("Login Successful")
else:
    print("Login Failed")

# Project 4: Calculate Factorial Using Functions

# Requirements
#    Accept a number
#    Create a factorial function
#    Return and display the result

# Sample Output
#     Enter Number: 5
#     Factorial: 120

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact

num = int(input("Enter Number: "))
print("Factorial:", factorial(num))