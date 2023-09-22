#write a program that checks  if a number is a primenumber or not

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print('its a prime number')
    else:
        print('it a not a prime.')