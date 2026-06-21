# Task-2: Python Decision Making & Functions

# Task 2.2: Create Reusable Functions

# Subtask 1: Define Functions with Parameters
# Concepts Covered
#    Function creation
#    Parameters and arguments

def square(num):
    print("Square =", num * num)

square(13)

# Subtask 2: Return Values from Functions
# # Concepts Covered
#    return statement
#    Function outputs

def multiply(a, b):
    return a * b

result = multiply(13, 43)
print("Result =", result)

#  Subtask 3: Use Default Parameters
# Concepts Covered
#    Optional arguments
#    Default values

def city(name="Hyderabad"):
    print("City:", name)

city()
city("Udaipur")

#  Subtask 4: Understand Function Scope
# Concepts Covered
#    Local variables
#   Global variables

college = "Arya College Of Engineering & Information Technology, Kukas, Jaipur. (ACEIT)"

def student():
    name = "Rishabh Parihar"
    print("College:", college)
    print("Student:", name)

student()