# Scientific calculator with basic arithmetic and scientific functions. 


import math

# Scientific Functions
sin = lambda x: math.sin(math.radians(x))
cos = lambda x: math.cos(math.radians(x))
tan = lambda x: math.tan(math.radians(x))
sqrt = math.sqrt
log = math.log10
pi = math.pi
pow = math.pow
radians = math.radians
degrees = math.degrees

print("===== Scientific Calculator =====")
print("Available Operations:")
print("+  -  *  /")
print("sin(x), cos(x), tan(x)")
print("sqrt(x)")
print("log(x)")
print("pow(x,y)")
print("pi")
print("radians(x)")
print("degrees(x)")
print("\nExamples:")
print("10 + 20 * 3")
print("sqrt(25) + 5")
print("sin(30) + cos(60)")
print("pi * 2")
print("pow(2,3) + 10")
print("\nType 'exit' to quit")

while True:
    expression = input("\nEnter Expression: ")

    if expression.lower() == "exit":
        print("Calculator Closed.")
        break

    try:
        result = eval(expression)
        print("Result =", result)

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except Exception:
        print("Invalid Expression!")