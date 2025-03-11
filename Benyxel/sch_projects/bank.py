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
        input = 
        self.account_bal += amount 
        rate = self.interest_rate * self.account_bal
        self.account_bal += rate
        
        print(f"\nDear! {self.account_holder}\nbe informed that the sum of GHS {amount} has been\nCredited into your account:{self.account_num}.\nInterest rate is GHS {rate},\nCurrent balance is GHS {self.account_bal}.\n")
    
    def withdraw(self, amount):
        charges = self.charges
        if self.account_bal < amount:
            print("Insufficient funds\n")
        elif amount + charges > self.account_bal:
            print("Insufficient funds\n")
        else:
            self.account_bal -= amount
            self.account_bal -= charges
            print(f"Dear! {self.account_holder}\nbe informed that the sum of GHS {amount} has been\nDebited from your account:{self.account_num}\nCharges : GHS {charges},\nCurrent balance is  GHS {self.account_bal}")
        
    def balance(self,):
        print(f"Your total balance is GHS {self.account_bal}")
        
    
     
        
class CheckingAcount(SavingAccount):
    def __init__(self,account_num,account_holder,balance=0,overdraft=0):
        SavingAccount. __init__(self,account_num,account_holder,balance=0,interest_rate = 0.01,charges=5.00)
        
        self.overdraft = overdraft
    
        
    def withdraw(self, amount):
        
        limit = self.overdraft
        limit = 500
        if self.account_bal < amount:
            print("Insufficient funds\n")
        elif amount > limit:
            print(F"You have reached your daily Limit {limit}")
        else:
            self.account_bal -= amount
            print(f"You have withdraw {amount}, current bal is {self.account_bal} ")
            
    
  
saving = SavingAccount(23456, "Yeboah B Bernard,")      
checking = CheckingAcount(23456, "Yeboah B Bernard,")

saving.deposit(100)
saving.withdraw(96)
checking.deposit(1200)
checking.withdraw(10)
checking.withdraw(1000)


