class Budget:
    def __init__(self, name):
        self.name = name
        self.income = 0
        self.expenses = 0
        
    def add_income(self, amount, description):
        self.income = self.income + amount
        print(f"Income added: {description} - Ksh {amount}")

    def add_expense(self, amount, description):
        self.expenses = self.expenses + amount
        print(f"Expenses added: {description} - Ksh {amount}")

    def show_balance(self,):
        result = self.income - self.expenses
        print(f"Balance: ksh {result}")

budget1 = Budget("Kuria")
budget1.add_income(50000, "Salary")
budget1.add_income(10000, "Freelance")
budget1.add_expense(2000, "WiFi")
budget1.add_expense(10000, "Rent")
budget1.show_balance()

budget2 = Budget("Steph")
budget2.add_income(40000, "Salary")
budget2.add_income(10000, "Freelance")
budget2.add_expense(1000, "WiFi")
budget2.add_expense(8000, "Rent")

import csv
with open("budg.csv", "w", newline="")as file:
    writer = csv.writer(file)

    # header row
    writer.writerow(["Name", "Income", "Expenses", "Balance"])

    for budget in [budget1, budget2]:
        balance = budget1.income - budget1.expenses
        writer.writerow([budget.name, budget.income, budget.expenses, balance])