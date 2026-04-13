#calculates federal income tax owed by income bracket

income = float(input("What was your 2025 income? "))

# tax brackets given by table
b1 = 11925
b2 = 48475
b3 = 103350
b4 = 197300
b5 = 250525
b6 = 626350

total_tax = 0

print("\nTax breakdown by income bracket: ")

# 10% bracket
if income > 0:
    taxable_income = min(income, b1)
    bracket_tax = taxable_income * 0.10 # applies the tax rate to the taxable income
    total_tax += bracket_tax # starts counting the total tax accumulated by bracket
    print(f"\nFirst $ {b1}: $ {bracket_tax:.2f}") #prints tax by bracket

# 12% bracket
if income > b1:
    taxable_income = min(income, b2) - b1
    bracket_tax = taxable_income * 0.12
    total_tax += bracket_tax
    print(f"$ {b1} - $ {b2}: $ {bracket_tax:.2f}")

# 22% bracket
if income > b2:
    taxable_income = min(income, b3) - b2
    bracket_tax = taxable_income * 0.22
    total_tax += bracket_tax
    print(f"$ {b2} - $ {b3}: $ {bracket_tax:.2f}")

# 24% bracket
if income > b3:
    taxable_income = min(income, b4) - b3
    bracket_tax = taxable_income * 0.24
    total_tax += bracket_tax
    print(f"$ {b3} - $ {b4}: $ {bracket_tax:.2f}")

# 32% bracket
if income > b4:
    taxable_income = min(income, b5) - b4
    bracket_tax = taxable_income * 0.32
    total_tax += bracket_tax
    print(f"$ {b4} - $ {b5}: $ {bracket_tax:.2f}")

# 35% bracket
if income > b5:
    taxable_income = min(income, b6) - b5
    bracket_tax = taxable_income * 0.35
    total_tax += bracket_tax
    print(f"$ {b5} - $ {b6}: $ {bracket_tax:.2f}")

# 37% bracket
if income > b6:
    taxable_income = income - b6
    bracket_tax = taxable_income * 0.37
    total_tax += bracket_tax
    print(f"Over $ {b6}: $ {bracket_tax:.2f}")

#prints total taxes owed
print(f"\nTotal tax owed: $ {total_tax:.2f}")

#calculate effective tax rate
effective_rate = (total_tax / income) * 100
print(f"Effective tax rate: {effective_rate:.1f}%")
