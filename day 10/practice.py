# PROJECT CALCULATOR USING DICTIONARY

# TODO: Write out thefunctions - addition, subtract, multiply and divide.

import art

def add(n1,n2):
    return n1+n2

def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# TODO: Add these 4 functions into a dictionary as the values.
# Keys = "+", "-", "*" and "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO: Use the dictionary operations to perform the calculations.
# output=operations["*"](2,3)

# print(output)
def calculator():
    print(art.logo)
    should_continue=True
    num1=float(input("Enter the first number:"))
    while should_continue:
        
        for key in operations:
            print(key)
        operation=input("pick one operation:")
        num2=float(input("Enter the second number:"))
        output=operations[operation](num1,num2)
        print(f"Result of {num1} {operation} {num2} :{output}")    


        choice=input(f"Type 'y' to continue with {output}, or Type 'n' to start new calculation: ")
        if choice=='y':
            num1=output
        else:
            should_continue=False
            print("\n"*20)
            calculator()  

calculator()