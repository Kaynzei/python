num1 = int(input('enter num1:'))
num2 = int(input('enter num2: '))
op = input('enter the operator: ')

if op == '+':
    print('the additon of', num1,'and',num2 ,'is', num1+num2)

elif op == '-':
    print('the substraction of', num1,'and',num2 ,'is', num1-num2)
elif op == '/':
    print('the division of', num1,'and',num2 ,'is', num1/num2)
elif op == '*':
    print('the product of', num1,'and',num2 ,'is', num1*num2)

else:
    print('invalid operator')