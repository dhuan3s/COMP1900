import random

# Welcome message
print("Welcome to TWENTY SLOTHS, good luck!")

# Track total games played and overall gain/loss
games_played = 0
net_gain_loss = 0
play_again = 1

# Main game loop (repeats until player quits)
while play_again == 1:
    games_played += 1
    print(f"\nGAME {games_played}")
    print("------")

    # Get and validate bet amount
    bet = float(input("\nEnter amount to bet: "))
    while bet < 10:
        bet = float(input("Bet must be at least $10, try again: "))

    # Subtract bet from net total (counts as loss)
    net_gain_loss -= bet

    # Initialize game state
    sloths = 1
    choice = 0

    # Game loop: continues until player holds or reaches/exceeds 20
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

        # Process choice and add sloths
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

    # Determine winnings based on final sloth count
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

    # Add winnings to net total
    net_gain_loss += winnings

    # Display final outcome message
    if sloths == 20:
        print("Amazing, you’re at exactly 20 sloths!")
    elif sloths > 20:
        print(f"Oh no, you’re at {sloths} sloths!")

    # Print winnings
    print(f"You won ${winnings:.2f}.", end=" ")

    # Print result summary (gain/loss)
    if winnings < bet:
        print("Congrats, you lost money :(")
    elif winnings == bet:
        print("You broke even.")
    else:
        print("Amazing, you gained money! :)")

    # Show overall stats
    print(f"Total games played: {games_played}")
    print(f"Net gain/loss: ${net_gain_loss:.2f}")

    # Ask if user wants to play again
    play_again = int(input("Enter 1 to play again, anything else to exit: "))

# Final message
print("Thanks for playing! Hope you came out ahead...")