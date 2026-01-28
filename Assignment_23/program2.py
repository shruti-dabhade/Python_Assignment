"""Write a Python program to implement a class named BankAccount with the following 
requirements:
• The class should contain two instance variables:
◦ Name (Account holder name)
◦ Amount (Account balance)
• The class should contain one class variable:
◦ ROI (Rate of Interest), initialized to 10.5
• Define a constructor (__init__) that accepts Name and initial Amount.
• Implement the following instance methods:
◦ Display() – displays account holder name and current balance

◦ Deposit() – accepts an amount from the user and adds it to balance
◦ Withdraw() – accepts an amount from the user and subtracts it from balance 
(Ensure withdrawal is allowed only if sufficient balance exists)
◦ CalculateInterest() – calculates and returns interest using formula: 
Interest = (Amount * ROI) / 100
• Create multiple objects and demonstrate all methods
"""


class BankAccount:
    ROI = 10.5  

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder Name:", self.Name)
        print("Current Balance:", self.Amount)

    def Deposit(self):
        amt = float(input("Enter amount to deposit: "))
        self.Amount += amt
        print("Amount deposited successfully")

    def Withdraw(self):
        amt = float(input("Enter amount to withdraw: "))
        if amt <= self.Amount:
            self.Amount -= amt
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest

Obj1 = BankAccount("Shruti", 5000)
Obj2 = BankAccount("Amit", 10000)


Obj1.Display()
Obj1.Deposit()
Obj1.Withdraw()
print("Interest:", Obj1.CalculateInterest())
Obj1.Display()


Obj2.Display()
Obj2.Deposit()
Obj2.Withdraw()
print("Interest:", Obj2.CalculateInterest())
Obj2.Display()
