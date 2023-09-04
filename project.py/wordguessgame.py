#In this game a word is randomly selected from a list. the word is assigned a variable chosen_word
#the user is asked to guess the letters of the word. if correct, it will replace the dashes in the word
#if after 6times of wrong guess,the user lose and the expected is printed.

import random

list = ['good','siamese', 'james','dodo', 'great','brown','kay','love','englsih','zebra','glory','love','sex','sexy']

dash =[ '-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-',]

chosen_word = random.choice(list)

#creat an empty list called display, for each word at the position in the chosen_word, add a '_' to the display. the dashes will be same number 
#so if choosen word was apple, the display should be ['-','-','-','-','-' with 5'-', representing the letter to guess.
display = []

for n in range(len(chosen_word)):
    display += '-'
print(display)

end_of_game = False
live = 6
while not end_of_game:
    guess = input('guess a letter:').lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        live -=1
        if live == 0:
            end_of_game = True
            print('You lose!')
            print('The chosen word is:',chosen_word)


    print(display)

    if '-' not in display:
        end_of_game = True
        print('you win.')

    
#This game is not complete yet. the user should be allowed to guess more and each letter enters the 
# appropriate position until the word is complete. and you can do that using while loop on the above block of code
