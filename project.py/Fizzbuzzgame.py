#in this game, each this person picks from num 1 down. if a participant picks a number that is divisible by 3, you
#dont mention the number. you say fizz. if its diisble by 5, you say buzz. if divisible in by both 3 & 5, you say fizz-buzz.
#That's exactly the game we are duplicating.
nu = input('enter a number from 1 to 20: ')
num = int(nu)
for number in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        print('Fizzbuzz')
        break
    if num % 3 == 0:
        print('Fizz')
        break
    if num % 5 == 0:
        print('Buzz')
        break

    else:
        print(num) 
        break
