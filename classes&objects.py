#python is an object oriented programming language
#class is a feature in python just like function. Myclass below is the name of the class

class Myclass:
    x = 5

p1 = Myclass()
print(p1.x)

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


name = input('Enter your name: ')
age = input('Enter your age: ')
p1 = person(name, age)
print(p1.name)
print(p1.age)

#to delete the age or the object from the above code
#del p1.age

