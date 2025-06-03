from abc import ABC, abstractmethod

class BankAccount(ABC):
    def _init_(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def _init_(self, account_number, account_holder, balance=0, interest_rate=0.01):
        super()._init_(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added interest {interest}. New balance is {self.balance}.")

class CheckingAccount(BankAccount):
    def _init_(self, account_number, account_holder, balance=0, overdraft_limit=500):
        super()._init_(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

# Example usage
savings = SavingsAccount( )
savings.deposit(200)
savings.withdraw(500)
savings.add_interest()

checking = CheckingAccount("CA456", "Yeboah", 500, 1000)
checking.deposit(300)
checking.withdraw(1000)
checking.withdraw(2000)