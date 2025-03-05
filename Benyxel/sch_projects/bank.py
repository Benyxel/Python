from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self,account_num,account_holder,balance=0):
        self.account_num = account_num
        self.account_holder = account_holder
        self.account_bal = balance
        
    def deposit(self, amount):
        pass
    def withdraw(self, amount):
        pass
    def balance(self, amount):
        pass
        
class SavingAccount(BankAccount):
    def __init__(self,account_num,account_holder,balance=0,interest_rate = 0.01):
        BankAccount.__init__(self,account_num,account_holder,balance=0)
        self.interest_rate = interest_rate  
    
    def deposit(self,amount):
        self.account_bal += amount 
        rate = self.interest_rate * self.account_bal
        self.account_bal += rate
        
        print(f"Dear! {self.account_holder},\n be informed that the sum of {amount} GHS has been\n Credited into your account:{self.account_num}.\nInterest is {rate}\n Current balance is {self.account_bal}")
    
    def withdraw(self, amount):
        if self.account_bal < amount:
            print("Insufficient funds")
        else:
            self.account_bal -= amount
            print(f"Dear! {self.account_holder},\nbe informed that the sum of {amount} GHS has been\nDebited from your account:{self.account_num}.\nCurrent balance is\n{self.account_bal}")
        
    def balance(self,):
        self.account_bal 
        print(f"Your total balance is {self.account_bal}")
        
        
class CheckingAcoount(SavingAccount):
    def __init__(self,account_num,account_holder,balance=0, overdraft=1000):
        SavingAccount.__init__(self,account_num,account_holder,balance=0,)
        self.limit = overdraft
    
    def withdraw(self, amount):
        if self.account_bal < amount:
            print("Insufficient funds")
        
            if self.account_bal < amount + self.limit:
                print("You have Reach your Daily limit")
            else:
                self.account_bal -= amount
                print(f"Dear! {self.account_holder}, \n be informed that the sum of {amount} GHS has been \n Debited from your account:{self.account_num}. \n Current balance is {self.account_bal}")

saving = SavingAccount(23456, "Yeboah B Bernard")
checking = CheckingAcoount(23456, "Yeboah B Bernard")
saving.deposit(12000)
saving.balance()
checking.withdraw(130)



