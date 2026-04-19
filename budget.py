# Endmonth Frugal budget

#basic needs
Rent = 10000
Electricity = 1700
WiFi = 2000
Water = 300
Garbage = 300

#Lifestyle
Shopping = 2000
Food = 7000
Entertainment = 3000
Fare = 2000
Laundry = 1000
Trans = 500
Family = 1000
Debts = 0
Others_Gas_etc = 0

# savings
Etica = 10000
Jubilee = 5000
Liquid = 2000


def basic_needs():
    total = Rent + Electricity + WiFi + Water + Garbage 
    return total

def lifestyle():
    total = Shopping + Food + Entertainment + Fare + Laundry + Trans + Family + Debts + Others_Gas_etc
    return total

def savings():
    total = Etica + Jubilee + Liquid
    return total

income = 49000

total_spent = basic_needs() + savings() + lifestyle()
deficit = income - total_spent
auto_deductions = Jubilee
to_withdraw_from_bank = total_spent - auto_deductions
cash = Rent + Water + Garbage + Fare + Laundry
survival = basic_needs() + lifestyle()


print(f"Total spent: {total_spent}")
print(f"Basic needs: {basic_needs()}")
print(f"Lifestyle: {lifestyle()}")
print(f"Survival amount is: {survival}")
print(f"Deficit left is: {deficit}")
print(f"Transfer to Mpesa: {to_withdraw_from_bank}")
print(f"Cash to withdraw: {cash}")
