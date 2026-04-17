# Define a function to print elements of list and check if end in s

def count_plurals(word_list): # Define function
    word_count = 0 # Words with s at the end count is created

    for word in word_list: # Loop to check each word in list
        print(word, end=" ") # Print each word in list
        if word[-1] == "s": # Checks if ends in 's' then adds to count
            print(" yes")
            word_count += 1
        else:
            print(" no")

    return word_count # Returns number of words that end in S

# Problem 2

result = count_plurals(['sloth', 'owls', 'sloths', 'bear', 'platypus']) # List of strings
print("Total:", result) # Prints return value of user-defined function