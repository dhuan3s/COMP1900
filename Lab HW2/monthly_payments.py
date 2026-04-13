principal = float(input("Please enter the following information:\n\tInitial amount of loan:  "))
apr = float(input("\tAnnual interest rate (in %): "))
term = float(input("\tTerm of payment (years): "))

r = float(apr / 100 / 12)
n = float(term * 12)

payment = principal * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
print(f"Monthly payment: ${payment:.2f}")
total = (payment*n)
print(f"\tTotal paid: ${total:.2f}")
interest_paid = (total - principal)
print(f"\tTotal interest paid: ${interest_paid:.2f}")