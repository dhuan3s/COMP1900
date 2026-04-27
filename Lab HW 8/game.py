# One player game using lists to distribute items

import random

def distribute(n, p):
    piles = []

    for i in range(p): # Goes through and create empty piles
        piles.append(0)

    for i in range(n): # Distribute items randomly
        pile_index = random.randrange(p) # Selects random pile
        piles[pile_index] += 1 # Adds 1 to random pile selected

    return piles

# take one turn without changing the original list
def take_turn(piles):
    new_piles = [] # Stores updated piles after removing one item
    items_taken = 0 # Counts how many items were removed

    for pile in piles: # Goes through each pile
        if pile > 0: # Only take from non-empty piles
            new_piles.append(pile - 1) # Removes one item from pile
            items_taken += 1 # Tracks removed items for new pile

    # Remove piles that became empty
    final_piles = []
    for pile in new_piles: # Checks updated piles
        if pile > 0:
            final_piles.append(pile) # Keeps non-empty piles

    # Adds new pile made from removed items
    if items_taken > 0: # Only add pile if items were taken
        final_piles.append(items_taken) # Adds the new combined pile

    return final_piles

# Get valid number of items
n = int(input("How many items do you have to distribute? "))
while n <= 0:
    n = int(input("Please enter a positive number of items: "))

# Get valid number of piles
p = int(input("How many piles should they be placed into? "))
while p <= 0:
    p = int(input("Please enter a positive number of piles: "))

piles = distribute(n, p) # Creates starting random piles
turn = 0 # Starting turn number
print("Turn", turn, ":", piles) # Displays initial game state

new_piles = take_turn(piles) # Takes first turn
while new_piles != piles: # Keeps going until state stops changing
    turn += 1 # Moves to next turn
    piles = new_piles # Updates current game state
    print("Turn", turn, ":", piles) # Shows updated piles
    new_piles = take_turn(piles) # Gets next turn state