#a program that produces random number as in case of dice. This is done with a module called random.randint(a,b)
#for the above to work, you first import random
import random

randominteger = random.randint(1, 10) #the random value will be within these numbers provided here
print(randominteger)

love_score = random.randint(1, 100)
print(f"your love score is {love_score}")
print('your love score is ',love_score)
