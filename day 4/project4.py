# rock paper scissor game
import random
choice_1 = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors: "))
if choice_1 == 0:
    print('''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif choice_1 == 1:
    print('''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')    
elif choice_1 == 2:
    print('''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')    
else:
    print("you typed wrong number")  
    exit()           
computer_choice = random.randint(0,2)
if computer_choice == 0:
    print('''computer choice:    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''') 
elif computer_choice == 1:
    print('''computer choice:    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')   
elif computer_choice == 2:
    print('''computer choice:    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')     
if choice_1 == computer_choice :
    print("its a draw!!")
elif choice_1 == 0 and computer_choice == 1:
    print("computer wins!!")
elif choice_1 ==0 and computer_choice == 2:
    print("You won!!")    
elif choice_1 == 1 and computer_choice == 0:
    print("You won!!")    
elif choice_1 == 1 and computer_choice ==2:
    print("computer won!!")
elif choice_1 == 2 and computer_choice == 0:
    print("computer won!!")
elif choice_1 == 2 and computer_choice == 1:
    print("You won!!")            

    