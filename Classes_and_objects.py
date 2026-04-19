class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance =  balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(self.balance)

class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        interest = self.balance *rate /100
        self.balance = self.balance + interest
        print(f"Interest added! New Balance: {self.balance}")

account1 = SavingsAccount("kuria", 1000)
account1.deposit(500)
account1.add_interest(10)