print("welcome to roller coster")
height = int(input("what is your height(in cm)?"))
if height>=120:
    print("you can ride the roller coster")
    age = int(input("what is your age?"))
    if age>18:
        print("you have to pay 12$")
    elif age>12 and age<=18:
        print("you have to pay 7$")
    else:
        print("you have to pay 5$")    
else:
    print("you can't ride the roller coster")