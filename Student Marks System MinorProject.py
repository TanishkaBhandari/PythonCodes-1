def changes():
    ip2=input('Do you want to add(a) or update(u) records? a/u')
    if ip2=='a':
        name=input('Enter new name')
        marks=int(input('Enter marks of new entry out of 100')) 
        mks[name]=marks
        print('Changes successful!')
        print(mks)
    elif ip2=='u':
        uname=input('Enter name of student to update')
        umarks=int(input('Enter marks updating entry out of 100')) 
        mks.update({uname:umarks})
        print('Successfully updated')
        print(mks)

def allOp():
    print('Maximum marks: ',max(mks.values())) 
    print('Maximum marks: ',min(mks.values()))
    print('Average marks: ',(sum(mks.values()))/3)
print('\tSTUDENT MARKS MANAGEMENT SYSTEM')
mks={'Rohit':100,'Tanishka':97,'Sifty':100}
print('Existing record:',mks)
ip=input('Do you want to modify record? y/n')
if ip=='y':
    changes()
elif ip=='n':
    print('Ok, bye!')
else:
    print('Invalid input. Please run again')

calc=int(input('''Select your desirable option: 1)View maximum marks 
               2) View minimum marks
               3) View average marks
               4) View all of the above
               5) NONE'''))
if calc==4:
    allOp()
elif calc==1:
    print('Maximum marks: ',max(mks.values())) 
elif calc==2:
     print('Maximum marks: ',min(mks.values()))
elif calc==3:
    print('Average marks: ',(sum(mks.values()))/3)
elif calc==5:
    print('Ok, bye!')
else:
    print('Invalid input. Please run again')