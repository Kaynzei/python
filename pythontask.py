#write a code that checks if the letter picked by a player is present in a randomly selected word picked from a list . assigned the variabe
#chosen_word to the picked variable
#asks the user to guess a word and assign ther answer to a variable called guess. make guess lowercase
#check if the word guessed(guess) is one of the word is  in the chosen_word
import random

list = ['gay','siamese', 'james','dodo', 'great','brown','kay']


chosen_word = random.choice(list)

guess = input('guess a letter:').lower()
for m in chosen_word:
    if guess == m:
        print('right')
    else:
        print('wrong')
