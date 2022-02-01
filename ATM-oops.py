import sys
class customer:
    bankname="SBI"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("after deposit:",self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print("insufficient")
            sys.exit()
        self.balance=self.balance-amt
        print("balance after draw:",self.balance)

print("Welcome",customer.bankname)
name=input("enter a name:")
c=customer(name)
while True:
    print("please select \n1.deposit \n2.withdrawl \n3.exit")

    option=int(input("enter a option:"))
    if option==1:
        amt=int(input("please enter a amount to deposit:"))
        c.deposit(amt)
        print("your total amount after depositing:",amt)
        
    if option==2:
        amt=int(input("enter a amount to withdrawl"))
        c.withdraw(amt)
        
    if option==3:
        print("thank you")
        sys.exit
