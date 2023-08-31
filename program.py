name = 'kanayo'

#print('my name is kanayo')
#print('kanayo is a boy')
#print('kanayo understands me' )
#print('kanayo never fails')

#VARIABLES AND DATA TYPES
#when printing a variable, no need for the quote

#joining variable and normal string together is called concatination

print(name + ' is a boy')
print(name + ' understands me')
print(name +' never fails')

age = 18

#whenever we are assigning a number to variable which is integer, we dont use quote as in the case of string above
#python cant concatinate integer with a string. but you can solve that by using comma instead usual +

print(name , "understands me  and he is" , age)
#the two commas are for joining string and integer
print(name ,' never fails even at ' , age)

#STRINGS
#special characters an still be exited with back slash

print('Hi , \'how are you')

# STRING FUCTIONS IN PYTHON

print(name[1]) #Used to access the 2nd character

#to convert uppercase and lower case
print(name.upper())
#to check is lower case or uppercase
print(name.islower())

#to check the amount/length of character in a variable or string

print(len(name))

print(name.index('n')) #printing the index number of any character in string

print(name.replace('y', 'b')) #replacing a character in the string

#NUMBERS IN PYTHON
print(max(4,2)) #for showinng the highest number 
print(bin(334)) #prints the binary string of a number

#there are some special function that will importation of the libary using math

from math import* #it means from maths import all(sqrt and it likes)

print(sqrt(45))

