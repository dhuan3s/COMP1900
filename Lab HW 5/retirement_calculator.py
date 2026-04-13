# Determines required investment to reach retirement goal

# Get and validate current age
current_age = int(input("Current age: "))
while current_age < 0:
    print("You have entered a negative age. Try again.")
    current_age = int(input("Current age: "))

# Get and validate starting balance
starting_balance = float(input("Starting balance: "))
while starting_balance < 0:
    print("You have entered a negative balance. Try again.")
    starting_balance = float(input("Starting balance: "))

# Get and validate retirement age
target_age = int(input("Target retirement age: "))
while target_age <= current_age:
    print("You have entered an invalid age. Try again.")
    target_age = int(input("Target retirement age: "))

# Get and validate target balance
target_balance = float(input("Target balance at retirement: "))
while target_balance < starting_balance:
    print("You have entered an invalid balance. Try again.")
    target_balance = float(input("Target balance at retirement: "))

# Get and validate yearly contribution increase
extra_per_year = float(input("Amount to increase annual contribution each year: "))
while extra_per_year < 0:
    print("You have entered a negative amount. Try again.")
    extra_per_year = float(input("Amount to increase annual contribution each year: "))

# Get and validate growth rate
expected_growth = float(input("Projected annual growth (percent): "))
while expected_growth < 0:
    print("You have entered a negative amount. Try again.")
    expected_growth = float(input("Projected annual growth (percent): "))

# Calculate number of years until retirement
years_remaining = target_age - current_age

# Start with year 1 contribution of $0.00
year1_contribution = 0

# Search for minimum contribution needed to reach target balance
while True:
    balance = starting_balance

    # Simulate growth for each year
    for i in range(years_remaining):
        growth = balance * expected_growth / 100
        extra = year1_contribution + extra_per_year * i
        balance = balance + growth + extra

    # Check if target is reached
    if balance >= target_balance:
        break

    # Increase contribution by $0.01 and try again
    year1_contribution += 0.01

# Display required contribution
print(f"To meet your retirement goal, you'll need to contribute ${year1_contribution:.2f}")
print(f"in year 1, increasing by ${extra_per_year:.2f} each year until retirement.")

# Display projected growth table
print("\nProjected growth:")
print("-----------------------------------------------")
print("Age   Year Start   Growth   Extra   Year End")

balance = starting_balance

# Loop through each year and display results
for i in range(years_remaining):
    age = current_age + i
    growth = balance * expected_growth / 100
    extra = year1_contribution + extra_per_year * i
    end_balance = balance + growth + extra

    print(f"{age}    $ {balance:.2f}    $ {growth:.2f}    $ {extra:.2f}    $ {end_balance:.2f}")

    # Update balance for next year
    balance = end_balance