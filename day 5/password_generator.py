import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8' '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many Symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []
for char in range(0,nr_letters):
    random_char = random.choice(letter)       
    password_list.append(random_char) 

# password += random.choice(letter):
# print(password)    


for char in range(0,nr_symbols):
    random_char = random.choice(symbols)
    password_list.append(random_char)

#password+= random.choice(symbols):
# print(password)

for char in range(0,nr_numbers):
    random_char = random.choice(numbers)
    password_list.append(random_char)
print(password_list)

##password+= random.choice(numbers):
# print(password)

random.shuffle(password_list)

print(password_list)
password = ""
for char in password_list:
    password += char
print("your password is:", password)    