total_income = int(input())
reported_tax = int(input())

total_tax = int(total_income * 0.20)
if reported_tax <0:
    print("Tax should be a non-negative integer.")
elif total_tax > reported_tax :
    print("STACY HAS COMMITTED TAX FRAUD")
else:
    print("Stacy has not committed tax fraud")
