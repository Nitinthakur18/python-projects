print("Welcome to the tip calculator")
x= float(input("what is the total bill?"))
y= float(input("how much tip you want to give(in %)?"))
y=x*(y/100)
x=x+y
print("x:",x)
z=int(input("how many people to split the bill"))
x=x/z
print("each person should pay:",round(x,2))

