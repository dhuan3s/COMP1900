# Collect age from user input as an integer and compute ticket price
# Updated to take multiple inputs to create order total

# Setting up variables for counter
below10_count = 0
child_count = 0
adult_count = 0
senior_count = 0

below10_total = 0
child_total = 0
adult_total = 0
senior_total = 0

# Asks for user input as long as age is non-negative
while True:
    age = int(input("Enter age of ticket holder (any negative value to exit): "))
    if age < 0:
        break
    # if statement makes sure that the age is a valid input
    if age > 122:
        print("That doesn't make any sense! Valid ages are 0-122.")
        continue
        # If statements correspond to table in assignment then assigns ticket price
    if age < 10:
        below10_count += 1
        below10_total += 0
    elif age <= 17:
        child_count += 1
        child_total += 23
    elif age <= 60:
        adult_count += 1
        adult_total += 29
    else:
        senior_count += 1
        senior_total += 25

# Prints out order summary

print("Order summary:")
print("---------------")
print(f"Below 10:\t{below10_count}", f"@ $0 each = $ {below10_total}")
print(f"10-17:   \t{child_count}", f"@ $23 each = $ {child_total}")
print(f"18-60:   \t{adult_count}",f"@ $29 each = $ {adult_total}")
print(f"Over 60: \t{senior_count}",f"@ $25 each = $ {senior_total}")


#total order cost
total = below10_total + child_total + adult_total + senior_total
print(f"\nTOTAL: ${total}")




