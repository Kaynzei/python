#looping through string

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index , letter)
    index = index +1

#counting letters

word = 'freedman'
count= 0

for letters in word:
    if letters == 'e':
        count= count + 1
print(count)

#slicing strings. note the space in between the words are counted too
s = 'Monty python'
print(s[0:4])

print(s[6:12])

print(s[8:])

print(s[:])