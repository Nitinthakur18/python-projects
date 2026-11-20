import random
names = ["Rohan", "Nitin", "Rohit", "Rahul", "Shashwat", "Virat", "Gandhi"]

# option 1
print(random.choice(names))

# option 2
random_index = random.randint(0,6)
print(names[random_index])