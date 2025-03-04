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
        
        print(f"{amount} Deposited. Interest is {rate} New Balance is {self.account_bal}")
        
saving = SavingAccount(23456, "Bernard,")
saving.deposit(1000)
saving.deposit(2000)


