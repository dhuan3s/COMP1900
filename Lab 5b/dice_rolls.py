# Lists possible values for two dices rolled


# Asks how many sides on each die
die1 = int(input("How many sides are on your first die?"))
die2 = int(input("How many sides are on your second die?"))

print("Possible rolls: ")

# Possible inputs for die1; range does not include the stop value so we add +1
for i in range(1, die1 + 1):
    j = 1
    #While loop to list possible values of die2. j is less than or equal to the num of sides on die2
    while j <= die2:
        print(i, ", ", j) # Print possible combo
        j += 1 # Moves the counter up

