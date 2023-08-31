import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', ' h', 'i', 'j', 'k', 'l', 'm','n','o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8','9']

symbols = ['*', '%','£', '!', '#', ' $', '>','?', '@', '+','<']

print('welcome to the Simple-KayPassword Generator')

no_letters =int(input('How many letters would you like in password:\n'))
no_symbols = int(input('How many symbols do you want in your password:\n'))
no_numbers = int(input('How many numbers do you want in your password:\n'))

#we have to open an empty string and keep adding those letters to the empty string. so if the user says he wants 4 letters, 
# we will take 4 letters randomly and add to the empty string. and print the string at the end.

password =""  #empty string

#so if the user says he wants 4, we will use range functiont to pick 4 things out of the above

for n in range(1, no_letters + 1):
    char = random.choice(letters) #generate the amount above randomly from letters
    password = password + char   #adding the randomly picked in char to the empty string

for n in range(1,no_symbols +1):
    char = random.choice(symbols)
    password = password + char

for n in range(1, no_numbers + 1):
    char = random.choice(numbers)
    password = password + char

print(password)


