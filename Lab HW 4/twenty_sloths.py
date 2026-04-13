import random

# Welcome message
print("Welcome to TWENTY SLOTHS, good luck!")

# Ask for bet amount and validate that it is at least $10
bet = float(input("\nEnter amount to bet: "))

while bet < 10:
    bet = float(input("Bet must be at least $10, try again: "))

# Player starts with 1 sloth
sloths = 1
choice = 0

# Continue game until player holds or reaches/exceeds 20 sloths
while sloths < 20 and choice != 3:
    print(f"\nCurrent sloths: {sloths}")
    print("1. Get 1-8 more sloths")
    print("2. Get 4-7 more sloths")
    print("3. Hold")

    # Get and validate user choice
    choice = int(input("\nEnter your choice (1, 2, or 3): "))

    while choice < 1 or choice > 3:
        print("\nInvalid choice.  Let’s try that again...")
        print(f"\nCurrent sloths: {sloths}")
        print("1. Get 1-8 more sloths")
        print("2. Get 4-7 more sloths")
        print("3. Hold")
        choice = int(input("\nEnter your choice (1, 2, or 3): "))

    # Process user choice
    if choice == 1:
        added = random.randint(1, 8)
        print(f"\nAdding {added}...")
        sloths += added

    elif choice == 2:
        added = random.randint(4, 7)
        print(f"\nAdding {added}...")
        sloths += added

    else:
        print(f"\nHolding at {sloths}...")

# Determine winnings based on final number of sloths
if sloths <= 14:
    winnings = 0
elif sloths == 15:
    winnings = bet * 0.25
elif sloths == 16:
    winnings = bet * 0.50
elif sloths == 17:
    winnings = bet * 1.00
elif sloths == 18:
    winnings = bet * 1.25
elif sloths == 19:
    winnings = bet * 1.50
elif sloths == 20:
    winnings = bet * 2.00
else:
    winnings = 0

# Print ending message for exact 20 or over 20
if sloths == 20:
    print("Amazing, you’re at exactly 20 sloths!")
elif sloths > 20:
    print(f"Oh no, you’re at {sloths} sloths!")

# Print winnings
print(f"You won ${winnings:.2f}.", end=" ")

# Print whether player lost money, broke even, or gained money
if winnings < bet:
    print("Congrats, you lost money :(")
elif winnings == bet:
    print("You broke even.")
else:
    print("Amazing, you gained money! :)")