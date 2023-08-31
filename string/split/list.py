#this tend to convert a string or range of number into list ,which 
#now makes it easier to count.

abc = 'With four words of love'
stuff= abc.split()
print(stuff)

print(len(stuff))
print(stuff[0])

#we can use split to collect a particular information from an email

#From kanayo4christ@gmail.com Sat Jan 23 2008

#if the above is in a file, you can open and loop.
fhand = open('string\split\email.txt', 'r')
for line in fhand:
    line = line.strip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[3])