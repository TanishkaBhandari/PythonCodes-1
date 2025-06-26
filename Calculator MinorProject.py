print('Calculator')
a=int(input('Enter 1st number'))
b=int(input('Enter 2nd number'))
op=input('Enter the operation(Type the symbols itself): +,-,/,*')
print('The answer is: ')
if op=='-':
    print(a-b)
elif op=='+':
    print(a+b)
elif op=='*':
    print(a*b)
elif op=='/':
    print(a/b)
else:
    print('Invalid input')