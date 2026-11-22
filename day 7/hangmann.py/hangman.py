import random
import hangman_words
from hangman_art import stages , logo

print(logo)
choosen_word = random.choice(hangman_words.word_list)


placeholder = ""
for i in choosen_word:
    placeholder = placeholder + "_"
# word_length = len(choosen_word)
# for position in range(word_length):
#     placeholder += "_"
print(placeholder)    

correct_letter = []
lives = 6
game_over = False
while not game_over:
    guess = input("guess the letter:").lower()
    print("your guess:",guess)
    if guess in correct_letter:
        print("You already guessed this letter")
        continue
    display = ""
    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:           #so that previous guessed letter can be present in output
            display +=letter    
        else:
            display += "_" 
    if guess not in choosen_word:
        lives -= 1
        print("you lose live,lives left:",lives)
        if lives == 0:
            game_over = True 
            print("you lose")
            print("the word was:",choosen_word)        
    print(display)       

    if "_" not in display:
        game_over = True
        print("you won")

    print(stages[lives])    