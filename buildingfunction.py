def greet(lang):
    if lang == 'migwo':
        print('urhobo')
    elif lang == 'otofe':
        print('ukwuani')
    else:
        print('unknown')

print('how are you my son? ')
print('i am fine mummy')
print('i think i may know your language greeting')
lang = input('enter ur language:')
greet(lang)
