# Collect age from user input as an integer and compute ticket price

# User inputs age
age = int(input("Enter your age: "))

#Outer if statement makes sure that the age is a valid input
if  0 <= age <= 122:
    # If statements correspond to table in assignment then assigns ticket price
    if age < 10:
        ticket_price = "free"
    elif age <= 17:
        ticket_price = "$23"
    elif age <= 60:
        ticket_price = "$29"
    else:
        ticket_price = "$25"
    print(f"Your ticket will be {ticket_price}, enjoy the Sloth Museum!")
else:
    print("That doesn't make any sense! Valid ages are 0-122.")
