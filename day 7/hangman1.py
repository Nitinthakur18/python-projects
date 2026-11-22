import random

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

word_list = ["apple", "mango", "papaya", "orange"]
choosen_word = random.choice(word_list)



# TODO-2 - Create an empty string called placeholder.
#  For each letter in the chosen_word, add a "_" to placeholder.
#  So if the chosen_word was "apple", placeholder should be "_____".
#  Print out placeholder.


placeholder = ""
word_length = len(choosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)    

# for i in choosen_word:
#     placeholder = placeholder + "_"


# TODO-3 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.


correct_letter = []
# TODO-4 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is, "Wrong" if it is not.

# TODO 4.0 Create an empty string called display.
# Loop through each letter in the chosen_word.
# If the letter at that position matches guess, reveal that letter in the display at that position.
lives =6
# If the letter at that position does not match guess, add a "_" to display.
# So if the user guessed "p" and the chosen_word was "apple", display should be "_pp__".
# Print display
game_over = False
while not game_over:
    guess = input("guess the letter:").lower()
    print("your guess:",guess)

    display = ""
    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter    
        else:
            display += "_"    
           
    if guess not in choosen_word:
        lives -=1
        print("wrong guess,lives left:",lives)
        if lives == 0:
            game_over = True 
            print("game over")
            print("you lose!!, the choosen word was:", choosen_word)
    
    print(display) 


    if '_' not in display:
        game_over = True
        print("you won!!!")       

    










