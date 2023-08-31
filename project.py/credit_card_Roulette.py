#Credit card Roulette is a game of chance where every party involved contributes their debit card into a hat or billfold
#The waitress or waiter will choose at random the card which will pay the entire bill
import random

name = input('enter the names separated by a comma:')
names = name.split(",")
print(names)
length = (len(names))
print(length)
random_choice = random.randint(0, length - 1)
print(names[random_choice], 'is paying for the food today')