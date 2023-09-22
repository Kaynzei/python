#the usefulness of function comes in when you dont want to rewrite a particular line of code over and over again. so you use a duxtion to keep calling it any time you want to use it.
def thing():
    print('i loyal boss')
    print('you are a good man')

thing()
print('the two lines of sentence above were his words, i can repeat them below for clarity')
thing()

#we have been using functions uknowingly; print is a function i.e why we open bracket and put things there. and many others too
#print function is reserved in def just like printf is defined and reserved in <stdio.h>
#the things you put inside the function parenthesis are called the argument

def kanayo(school):
    if school == 'auntylyn':
        print('we are colleague in ', school)
        print('nice meeting you')

print('i am glad to be at this arena')
name = input('what is your name: ')
school = input('which school do you attend:')
kanayo(school)

#another way of using function
def greet_function(name, age):
    print(f"welcome {name} '. you are  {age} years old.")

greet_function(name= 'john', age=27)


def add_number(num1,num2):
    return num1 + num2

num1 = int(input('enter the first number: ')) #if you dont convert it, python will see it as string and just appose them
num2 = int(input('enter the second number: '))
print(add_number(num1, num2))


#difference between function parameter and argument. parameter is the variable declared inside the function,
# argument is the provided value of that variable.