class ATM:
    def __init__(self, pin, balance=0):#AUTOMATICALLY RUNS AS CONSTRUCTOR WHEN NEW OBJ CREATED 
        self.pin = pin
        self.balance = balance


    def insert_card(self):
        #print(self) object’s memory address shows up
        if 'card'==input('Insert your card '):
            print('Welcome! ')
            return True #to make next method run, return true to if statement
        else:
            print('Invalid card')
            return False
        


    def verify_pin(self):
        if self.pin==int(input('Enter your pin ')):
            return True
        else:
            print('OOPS! Wrong pin')
            return False
            

    def show_menu(self):
        while True:
            print("\nSelect operation:\n1) Check balance\n2) Cash withdraw\n3) Exit")
            choice = input("Choose 1, 2 or 3: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                print("Thank you. Please take your card.")
                break
            else:
                print("Invalid option, try again.")

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")
        #{self.balance} gets replaced by the current value of self.balance.


    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Amount must be a number.")
            return

        if amount <= 0:
            print("Enter a positive amount.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance = self.balance - amount
            print(f"Please take your cash. New balance: {self.balance}")


def main():
    atm = ATM(pin=1234, balance=1000)#CREATING AN OBJECT OF THE CLASS
    print("\t\tWelcome to PNB")
    if atm.insert_card():
        if atm.verify_pin():#runs if true comes 
            atm.show_menu()


