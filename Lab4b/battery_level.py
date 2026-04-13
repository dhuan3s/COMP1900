# Prompts user to input battery level, tests for valid int within range

battery_level = int(input("Enter battery level (0-100): ")) # Asks user for battery level as input

while battery_level not in range(0,100): # Runs if user input is not within range of 0-100
    print("Battery level must be between 0 and 100, try again: ") # Gives user an error message as val is outside of range
    battery_level = int(input("Enter battery level (0-100): ")) # Asks for user input again

print("Battery level accepted, exiting now...") # If battery level is within range, prints the following
quit() # Ends the program running
