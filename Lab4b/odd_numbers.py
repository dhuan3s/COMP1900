# Counts all the odd numbers leading up to user specified value
n = int(input("Enter a positive integer: ")) # Asks user for positive integer
num = 1 # Starts the count for odd numbers at 1

while n < 0: # Tests to see if integer entered is a positive value
    print("Must be a positive integer, try again.") # If not, user is prompted to try again with a valid positive integer
    n = int(input("Enter a positive integer: "))

print(f"\nOdd numbers up to {n}:") # If n > 0, the above while loop is skipped and begins to print the odd numbers up to n

while num <= n: # This loop only runs while the counter is less than value entered, basically counting up to the input val
    if num % 2 != 0: # Using the modulo operation to check for odd numbers
        print(num)
    num += 1 # Moves the loop forward so that num does not stay equal to 1

