import random

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

while True:

    print("\n----- ROCK PAPER SCISSORS -----")
    print("0 for Rock")
    print("1 for Paper")
    print("2 for Scissors")

    your_choice = int(input("Enter your choice: "))

    # Generate computer choice
    computer_choice = random.randint(0, 2)

    # Display choices
    if your_choice not in [0, 1, 2]:
        print("Invalid choice! Please enter 0, 1 or 2.")

    else:
        print("Your choice:", choices[your_choice])
        print("Computer choice:", choices[computer_choice])

        # Winning conditions
        if (your_choice == 0 and computer_choice == 2) or \
           (your_choice == 2 and computer_choice == 1) or \
           (your_choice == 1 and computer_choice == 0):

            print("You won!")
            user_score += 1

        elif your_choice == computer_choice:
            print("It's a draw!")

        else:
            print("You lose!")
            computer_score += 1

        # Display scores
        print("\n----- SCOREBOARD -----")
        print("Your score:", user_score)
        print("Computer score:", computer_score)

    # Replay option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\n----- FINAL SCORE -----")
print("Your score:", user_score)
print("Computer score:", computer_score)
print("Thanks for playing!")