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
    def __init__(self,account_num,account_holder,interest_rate=0.01):
        super().__init__(self,account_num,account_holder,balance=0)
        self.interest_rate = interest_rate  
    
    def deposit(self,amount):
        self.account_bal += amount
        print(f"{amount}. New Balance is {self.account_bal}")
        
saving = SavingAccount(000000, "Bernard", 3000)
saving.deposit(200)
print(saving)