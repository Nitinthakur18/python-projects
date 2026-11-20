print("welcome to python pizza delivery ")
size= input("what size of pizza do you want? S, M or L:")
pepperoni = input("do you want pepperoni on your pizza? Y or N:")
extra_chesse = input("do you want extra chesse on your pizza? Y or N:")
bill = 0
if size == "S":
    bill = 15
    print("you have to pay $15 for pizza")
    if pepperoni == "Y":
        bill = bill +2

elif size == "M":
    bill = 20
    print("you have to pay $20 for pizza")
    if pepperoni == "Y":
        bill = bill+3 
elif size == "L":
    bill = 25
    print("you have to pay $25 pizza")
    if pepperoni == "Y":
        bill = bill+3 
else :
    print("you typed wrong inputs.")       
     
if extra_chesse =="Y":
    bill = bill +1  
print("your total bill is $", bill)    

