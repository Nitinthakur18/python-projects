import art
print(art.logo)
# x=float(input("What's the first number?:"))
# print("+\n-\n*\n/\n")
# operation=input("choose an operation:")
# y=float(input("what's the next number?:"))


def calculator(x,operation,y):
    if operation=='+':
        return x+y
    elif operation=='-':
        return x-y
    elif operation=='*':
        return x*y
    elif operation=='/':
        return x/y
    elif operation=='%':
        return x%y
    else:
        return "Enter valid operation from above choice"


want_to_continue=True
while want_to_continue:
    num1=float(input("What's the first number?:"))
    should_continue=True
    while should_continue:
        print("+\n-\n*\n/\n%\n")
        operation=input("choose any one operation: ")
        num2=float(input("what's the next number?:"))

        output=calculator(num1,operation,num2)
        print("Result:",output)

        y_or_n=input(f"Type 'y' to continue calculating with {output}, ""or type 'n' to start a new calculation: ")
        if y_or_n=='y':
            num1=output
        else:
            should_continue=False    