# Returns tip dollar amount based on level of service

def tip_amount(bill_total, service_level): # Define tip_amount func

    bill_total = float(bill_total) # Declares bill total as a float
    service_level = str(service_level) # Service level is a string

    # Sets tip percentage using service level
    if service_level == "poor":
        tip_percent = 0.10
    elif service_level == "good":
        tip_percent = 0.18
    elif service_level == "excellent":
        tip_percent = 0.25
    else:
        tip_percent = 0.15

    # Calculate tip amount based on if statements above assigning percentage
    tip_amount = bill_total * tip_percent
    return tip_amount

# Question 2

# Read user input before calling function
service_level = input("How was your service today? ")
bill_total = float(input("What is the total bill amount? "))
print(f"{tip_amount(bill_total, service_level):.2f}") # Prints tip amount rounded to two decimal places
