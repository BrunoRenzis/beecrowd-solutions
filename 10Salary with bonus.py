SellerName = input("")
FixedSalary = float(input())
SalesTotal = float(input())
Bonus = 0.15
FinalSalary = 0

FinalSalary = FixedSalary + (SalesTotal * Bonus)

print("TOTAL = R$ %.2f"% FinalSalary)