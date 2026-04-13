# Checks to see if user input is correct password and displays remaining attempts

# Correct password is snoopy
correct_password = "snoopy"

#Attempts allowed
max_attempts = 4

# Counter for wrong attempts
attempts = 0

# Looping until sentinel value OR run out of attempts
while attempts < max_attempts:

    password = input("Enter password: ")

    if password == correct_password:
        print(f"Access granted.")
        break

    #Starts counting down if input password is incorrect
    else:
        attempts += 1
        attempts_left = max_attempts - attempts

        # Asks user to try again if they have attempts left
        if attempts_left > 0:
            print(f"Incorrect password. You have {attempts_left} attempt(s) left.")

        #if no attempts left, loop ends and tells user account is locked
        else:
            print(f"Access denied. You have been locked out of your account. Please try again later.")
