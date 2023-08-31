#write a program that calculates the average student height from a list of heights
#the average height should be rounded to the nearest whole number
#Rule: you cant use the len() and sum() function. use forloop

#write a program that prints the maximum value from a list

nums = [45, 45, 87, 78, 35, 99, 3, 72]

highest_number = -1
for neck in nums:
    if neck > highest_number:
        highest_number = neck
print(highest_number)

lowest_number = 50
for head in nums:
    if head < lowest_number:
        lowest_number = head
print(lowest_number)

#range loops trough the two sets of number given leaving the last number e.g  range (0, 10)will print 0 to 9 or u can (0,10,3) which 
# means u will print every 3rd number.
#Then u can do anything with the numbers, just below is addition of the numbers. and in the below, u declare 
#a variable and everything will be added to the variable .

total = 0
for n in range(lowest_number, highest_number +1):
    total = total + n
print(total)

#write a program that adds all even number between 1 to 100

total_even = 0
for number in range(2, 101,2):
    total_even = total_even + number
print(total_even)

#or

total_evenn = 0
for num in range(1,101):
    if num % 2 == 0:
        total_evenn = total_evenn + num
print(total_evenn)

