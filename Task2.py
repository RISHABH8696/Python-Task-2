# Task-2: Python Decision Making & Functions

# Task 2.1: Conditional Statements

# Subtask 1: Write if-else Programs
# Concepts Covered
#    if statement
#    else statement
#    Decision making


# 1st Subtask: Check whether a number is positive or negative

num = int(input("Enter a number: "))
if num >= 0:
    print(num, "is a positive number")
else:
    print(num, "is a negative number")

# 2nd Subtask: Check whether a person is eligible to vote

age = int(input ("Enter your age:"))
if age >= 18:
    print("you are Eligible for voteing")
else:
    print("Now, you are not eligible for voteing")

# 3rd Subtask: Check whether a number is even or 

num = int(input("Enter a number:"))

if num % 2 == 0:
    print(num, "is a Even number")
else:
    print(num, "is a Odd number")

# Subtask 2: Implement Nested if Conditions
# Concepts Covered
#    Nested decision making
#    Multiple levels of validation


# 1st subtask: Check eligibility for college admission based on marks and age

age = int(input("Enter Age: "))
marks = int(input("Enter Marks: "))

if age >= 17:
    if marks >= 60:
        print("Admission Granted")
    else:
        print("Marks Too Low")
else:
    print("Age Not Eligible")

# 2nd subtask: ATM withdrawal validation

balance = 13000000000
amount = int(input("Enter Amount: "))

if amount <= balance:
    if amount > 0:
        print("Withdrawal Successful")
    else:
        print("Invalid Amount")
else:
    print("Insufficient Balance")

# 3rd subtask: Determine employee bonus eligibility

experience = int(input("Years of Experience: "))

if experience >= 5:
    if experience >= 10:
        print("Bonus: ₹10000")
    else:
        print("Bonus: ₹5000")
else:
    print("No Bonus")

#  Subtask 3: Use elif Statements
# Concepts Covered
#    Multiple condition checking
#    Decision chains

# 1st subtask: Student grade classification

marks = int(input("Enter Marks: "))

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
    
# 2nd subtask: Traffic signal simulation

signal = input("Enter Signal Color: ")

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Wait OR Ready to Go and Prepare to Stop")
elif signal == "green":
    print("Go")
else:
    print("Invalid Signal")

# 3rd subtask: Weather recommendation system

weather = input("Enter Weather: ")

if weather == "sunny":
    print("Wear Sunglasses")
elif weather == "rainy":
    print("Take Umbrella")
elif weather == "cold":
    print("Wear Jacket")
else:
    print("Stay Safe")

# Subtask 4: Handle Multiple Conditions
# Concepts Covered
#    and
#    or
#    not

# 1st subtask: Login validation

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")

# 2nd subtask:  Loan eligibility checker

age = int(input("Age: "))
income = int(input("Income: "))

if age >= 21 and income >= 30000:
    print("Loan Approved")
else:
    print("Loan Rejected")

# 3rd subtask:  Scholarship eligibility system

cgpa = float(input("CGPA: "))
extracurricular = input("Extracurricular Activities (yes/no): ")
if cgpa >= 3.5 and extracurricular.lower() == "yes":
    print("Scholarship Awarded")
else:
    print("Scholarship Not Awarded")

