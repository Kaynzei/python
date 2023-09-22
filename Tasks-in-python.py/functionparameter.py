#demonstrating keyword argument in function.
def introduction(name, state, age):
    print(f'welcome mr {name}, how is your family.')
    print(f'we are glad to hear that you from {state} and with a age number of {age}.')


print('Who are you and how can we help you?')
a = input('what is ur name: ')
b = input ('How old are you: ')
c = input('Which state are you from: ')

introduction(name = a, age = b, state = c)
