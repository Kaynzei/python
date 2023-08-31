n = 5
while n > 0 :
    print(n)
    n = n -1
print('done')

#breaking out of a loop
#while true is commonly used in a string
    
while True:
    line = input('are u still schooling? : ')
    if line == 'done':
        print('so you are', line)
        break
    elif line == 'still schooling':
        print('since you are', line)
        print('i would like you to be my study partner')
        question = input('are you okay with it? : ')
        if question == 'yes':
            break
        if question == 'no':
            print('Thanks for audience')
            break
print('That is okay')

#continue in loop

while True:
    line2 = input('do you love me? :')
    if line2 == 'yes':
        continue
    if line2 == 'no':
        break
print('goodbye')

#definite loop( i.e forloop)take i to be the variable, in as =
for i in ('emeke', 'kanayo'):
    print(i)

#another example of forloop
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New year ', friend)
print('thanks all')

#finding the largest number using forloop

largest_so_far = -1
print('before', largest_so_far)
for unknown_num in (9, 41, 12, 3, 74, 15) :
    if unknown_num > largest_so_far:
        largest_so_far = unknown_num
    print(unknown_num, largest_so_far)
print('After', largest_so_far,)


#print a program that adds 5dollar tax to every customer after the calculation of their bill


add = 5
for final_bill in [50 , 46 , 80, 100]:
    final_bill= final_bill + add
    print(final_bill)

#you can loop through a list , dict by using forloop
my_dict = {
    'name': 'Tim',
    'nationality' : 'African',
    'Qualification' : 'College',
    'age': 87,
    'friends' : ['peter','paul', 'precious']
}

for x in my_dict:
    print(my_dict)
    if my_dict == 'age':
        break

#you can also loop through a number
for n in range(6, 8):
    print(n)

#nested loop is forloop in for loop

my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(my_list)
