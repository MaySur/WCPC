# Prompt the user for Stacy's income and deduction
income = int(input("Income: "))
reported_tax = int(input("Tax: "))

# Calculate the total tax amount Stacy should have paid
total_tax = (income * 0.20)

if total_tax > reported_tax :
    print("STACY HAS COMMITTED TAX FRAUD")
else:
    print("Stacy has not committed tax fraud")
