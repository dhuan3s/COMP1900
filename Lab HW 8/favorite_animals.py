# Collects favorite animal survey responses and shows results

animals = {} # Stores animals and response counts
survey_num = 1 # Starts survey counter
animal = input("Enter favorite animal from survey #" + str(survey_num) + ": (X to exit) ").lower()  # Gets first survey response

while animal != "x": # Continues until user exits
    if animal in animals: # Checks if animal already entered
        animals[animal] += 1 # Adds to existing count
    else:
        animals[animal] = 1 # Starts count for new animal

    survey_num += 1 # Moves to next survey
    animal = input("Enter favorite animal from survey #" + str(survey_num) + ": (X to exit) ").lower()

# Prints summary of all responses
print("Summary of responses:")

for animal in animals: # Goes through each animal
    print(animal, "-", animals[animal])

highest = 0 # Stores largest response count

for animal in animals: # Finds highest count
    if animals[animal] > highest:
        highest = animals[animal]

# Prints animal(s) with most votes
print("Most popular animal(s):")

for animal in animals: # Checks for tied winners
    if animals[animal] == highest:
        print(animal)