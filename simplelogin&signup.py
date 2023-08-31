#simple login and signup 

print('create your account Now!')
username = input('Enter username: ')
password = input('Enter password: ')

print('your account has been successfully created')
print('you can Log in now.')
username2 = input('Enter username: ')
password2 = input('Enter password: ')

if username == username2 and password == password2:
    print('Logged in successfully')
else :
    print('Invalid credentials')