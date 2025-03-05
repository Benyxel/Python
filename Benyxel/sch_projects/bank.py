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
    def __init__(self,account_num,account_holder,balance=0,interest_rate = 0.01,charges=5.00):
        BankAccount.__init__(self,account_num,account_holder,balance=0,)
        self.interest_rate = interest_rate 
        self.charges= charges 
    
    def deposit(self,amount):
        self.account_bal += amount 
        rate = self.interest_rate * self.account_bal
        self.account_bal += rate
        
        print(f"\nDear! {self.account_holder},\nbe informed that the sum of GHS {amount} has been\nCedited into your account:{self.account_num}.\nInterest rate is GHS {rate},\nCurrent balance is GHS {self.account_bal}.\n")
    
    def withdraw(self, amount):
        if self.account_bal < amount:
            print("Insufficient funds")
        else:
            self.account_bal -= amount
            charges = self.charges
            self.account_bal -= charges
            print(f"Dear! {self.account_holder},\nbe informed that the sum of GHS {amount} has been\nDebited from your account:{self.account_num}\nCharges : GHS {charges},\nCurrent balance is  GHS {self.account_bal}")
        
    def balance(self,):
        print(f"Your total balance is GHS {self.account_bal}")
        
        
class CheckingAcount(BankAccount):
    def __init__(self,account_num,account_holder,balance=0,overdraft = 500):
        BankAccount.__init__(self,account_num,account_holder,balance=0,)
        self.overdraft = overdraft
        
    def deposit(self, amount):
        self.account_bal += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")    
        
checking = CheckingAcount(23456, "Yeboah B Bernard")
checking.deposit(200)


