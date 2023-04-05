total_income = int(input())
reported_tax = int(input())

total_tax = int(total_income * 0.20)
if total_tax > reported_tax :
    print("STACY HAS COMMITTED TAX FRAUD")
else:
    print("Stacy has not committed tax fraud")
