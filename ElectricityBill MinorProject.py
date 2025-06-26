print('Electricity bill generator')
ut=int(input('Enter the units of electricity consumed'))
if ut<100 or ut==100:
    print('No bill')
elif ut>100 and ut<500:
    print('Bill is Rs. 300')
elif ut==500:
    print('Bill is Rs. 300')
elif ut>500 and ut<700:
    print('Bill is Rs. 500')
elif ut==700:
    print('Bill is Rs. 500')
else:
    print('Bill is Rs. 800')