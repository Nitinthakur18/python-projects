import random

random_integer = random.randint(1,8) #to return random number between 1 and 8 including both of them (a<=x<=b)
print(random_integer)
random_float = random.random() # to return random floating number between 0 and 1 including o (0.0<=x<b) 
print(random_float)
random_range = random.randrange(1,7) # to return integer from a to b including a only (a<=x<b)
print(random_range)
random_uniform = random.uniform(1,5) # to return floating point number between 1 and 5 (a<=x<=b)
print(random_uniform)
list = [56,78,34,98,67,23,43,59]
print(random.choice(list)) # to return list





random_float = random.random()*10  # to return random floating number between 0 and 1 including o (0.0<=x<b) AND MULTIPLIED BY 10
print(random_float)

coin = ["heads", "tails"]
print(random.choice(coin))