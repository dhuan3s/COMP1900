#Read user input and prints all negative-indices of string

user_input = str(input("Enter a string: ")) # User inputs string

length = len(user_input) # Determines length of user input
i = 0 # Sets index counter at 0
line = 0 # Line indicator starts at 0

while i < length: # Runs until there are no characters left in the string input
    print(line, user_input[i], user_input[:i+1]) # Prints line num, character at index, and string up to index val
    line += 1 # moves line counter up
    i = i + 1 # moves onto next character
