class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks  # Expecting a dictionary or list of marks
        
    def changes(self):
        ip2=input('Do you want to add(a) or update(u) records? a/u ')
        if ip2=='a':
            subj=input('Enter new subject ')
            mks=int(input('Enter marks of new subject out of 100 ')) 
            self.marks[subj]=mks
            print('Changes successful!')
            print('New record:',self.name,self.roll,self.marks)
        elif ip2=='u':
            usubj=input('Enter subject to update ')
            umarks=int(input('Enter marks out of 100 ')) 
            self.marks.update({usubj:umarks})
            print('Successfully updated')
            print('Updated record:',self.name,self.roll,self.marks)
        
        
    def allOp(self):
        print('Maximum marks: ',max(self.marks.values())) 
        print('Maximum marks: ',min(self.marks.values()))
        print('Average marks: ',(sum(self.marks.values()))/3)
        pass

    def display_report(self):
        print('Name of student: ',self.name)
        print('Roll Number: ',self.roll)
        print('Marks: ',self.marks)
        print('Average marks: ',(sum(self.marks.values()))/3)
        pass
    
    


def main():
    print('\tSTUDENT MARKS MANAGEMENT SYSTEM')
    std=Student('Tanishka',40,marks={'C':87,'DSA':93,'Java':95})
    
    print('Existing record:')
    std.display_report()
    
    ip=input('Do you want to modify record? y/n ')
    if ip=='y':
        std.changes()
    elif ip=='n':
        print('Ok')
    else:
        print('Invalid input. Please run again')
        
    calc=int(input('''Select your desirable option: 1)View maximum marks 
               2) View minimum marks
               3) View average marks
               4) View all of the above
               5) NONE '''))
    
    if calc==4:
        std.allOp()
    elif calc==1:
        print('maximum marks: ',max(std.marks.values())) 
    elif calc==2:
        print('maximum marks: ',min(std.marks.values()))
    elif calc==3:
        print('average marks: ',(sum(std.marks.values()))/3)
    elif calc==5:
        print('Ok, bye!')
    else:
        print('Invalid input. Please run again')
    
    print('Final Record: ')
    std.display_report()
    pass


if __name__ == "__main__":
    main()