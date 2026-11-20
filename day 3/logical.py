print("welcome to roller coster")
height = int(input("what is your height(in cm)?"))
bill = 0
if height>=120:
    print("you can ride the roller coster")
    age = int(input("what is your age?"))
    if age>=45 and age<=55:
        bill = 0
        print("you have to pay",bill)  
    elif age>=18:
        bill = 12
        print("adult tickets are 12$")   
    elif age>12:
        bill = 7
        print("youth ticket are 7$")
    else:
        bill = 5
        print(" child tickets are 5$")

    want_photos=(input("do you want to take photos? type y for yes and n for no: "))
    if want_photos =="y" and age <45 and age>55:
        bill = bill + 3 #bill+=3
        
    print("your final bill is",bill)
    
        


else:
    print("you can't ride the roller coster")