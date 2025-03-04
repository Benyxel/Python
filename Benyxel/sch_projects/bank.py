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
        
        print(f"Dear! {self.account_holder}, be informed that the sum of {amount} GHS has been Credited into your account:{self.account_num}. Interest is {rate} Current balance is {self.account_bal}")
    
    def withdraw(self, amount):
        if self.account_bal < amount:
            print("Insufficient funds")
        else:
            self.account_bal -= amount
            print(f"Dear! {self.account_holder}, be informed that the sum of {amount} GHS has been Debited from your account:{self.account_num}. Current balance is {self.account_bal}")
        
    def balance(self,):
        self.account_bal 
        print(f"Your total balance is {self.account_bal}")
class CheckingAcoount(BankAccount):
    def __init__(self,account_num,account_holder,balance=0, overdraft=1000):
        BankAccount.__init__(self,account_num,account_holder,balance=0,)
        self.limit = overdraft
    
    def deposit(self,amount):
        self.account_bal += amount 
        rate = self.interest_rate * self.account_bal
        self.account_bal += rate
        print(f"Dear! {self.account_holder}, be informed that the sum of {amount} GHS has been Credited into your account:{self.account_num}. Interest is {rate} Current balance is {self.account_bal}")
    
    def withdraw(self, amount):
        if self.account_bal < amount + self.limit:
            print("You have Reach your Daily limit")
        else:
            self.account_bal -= amount
            print(f"Dear! {self.account_holder},\n. be informed that the sum of {amount} GHS has been\n. Debited from your account:{self.account_num}.\n. Current balance is {self.account_bal}")

saving = SavingAccount(23456, "Yeboah B Bernard")
checking = CheckingAcoount(23456, "Yeboah B Bernard")
saving.deposit(2000)
saving.deposit(2000)
"""saving.withdraw(3000)
saving.balance()"""

checking.withdraw(5668)



