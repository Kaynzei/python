#inheritance means taking from existing class and putting it in another class.
#below,new1 is the name of the file without adding py, then student is the name of the class we are importing. person is the name of our new class.
#you write pass if you dont have anything yet to put in the class.


from new1 import student

class person(student):
    pass

p1 = person()
print(p1.name)