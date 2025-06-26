def start():
     if pin==int(input('Enter your pin')):
        print('Press: 1)Check balance/n 2)Cash withdraw')
        operation()
     else:
        print('Wrong pin')

def operation():
    option=int(input('Select your option'))
    if option==1:
            print('Your current balance is Rs. ',amount)
    elif option==2:
            amt=int(input('Enter amount to withdraw'))
            print('Current balance is Rs. ',amount-amt)
    else:
        print('Invalid option')
        
amount=10000
pin=1234
print("\t\tWelcome to PNB")
if 'card'==input('Insert your card'):
    print('Welcome')
    start()
else:
    print('Invalid Card')