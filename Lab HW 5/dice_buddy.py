import random

# Main loop: keeps running until user enters non-positive values
while True:
    # Get number of dice from user
    dicenum = int(input("Number of dice to roll (any non-positive value to exit): "))
    if dicenum <= 0:
        break

    # Get number of sides per die
    numsides = int(input("Number of sides per die (any non-positive value to exit): "))
    if numsides <= 0:
        break

    # Display what is being rolled
    print(f"Rolling {dicenum} dice with {numsides} sides...")

    # Initialize total sum of dice
    total = 0

    # Loop through each die and simulate a roll
    for i in range(1, dicenum + 1):
        roll = random.randint(1, numsides)
        print(f"Die {i}: {roll}")
        total += roll

    # Display total of all dice
    print(f"Total: {total}")