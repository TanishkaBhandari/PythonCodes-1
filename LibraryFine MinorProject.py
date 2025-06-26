from datetime import date
print('Library fine calculator')
fday=input('Enter the date you issued book on')
today = date.today()
days= today-fday 
if days==0 or days<=7:
    print('No fine')
elif days>7 and days<10:
    print('Fine to be paid is Rs.10')
elif days>10:
    print('Fine to be paid is Rs.50')
else:
    print('Invalid input')