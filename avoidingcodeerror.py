#there are sometimes your code encounter an error and it stops running.it stops the whole code from running
#to avoid the above scenario use try and except

try:
    x = int(input('enter an integer:'))
    print(x)
except:
    print('value not an integer')