#counting lines in a file
fhand = open('dictionary.py', 'r')
count = 0
for lines in fhand:
    count = count + 1
    print('line count:', count)
fhand.close
#you can use len character for tehe above and the amout of the word in a file before deciding whteher to read.
 