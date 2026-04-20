def contains_only_digits(text):
    # return False if empty string
    if len(text) == 0:
        return False

    # check each character
    for char in text:
        if char < '0' or char > '9':
            return False

    return True

def luhn_satisfied(number_string):
    # first check if valid digits
    if not contains_only_digits(number_string):
        return False

    total_sum = 0
    should_double = False

    # loop from right to left
    for i in range(len(number_string) - 1, -1, -1):
        digit = int(number_string[i])

        if should_double:
            digit = digit * 2

            if digit > 9:
                digit -= 9

        total_sum += digit

        # flip doubling flag
        should_double = not should_double

    # check if divisible by 10
    return total_sum % 10 == 0

# test contains_only_digits
print(contains_only_digits("1234"))     # True
print(contains_only_digits(""))         # False
print(contains_only_digits("12e4"))     # False
print(contains_only_digits("sloth"))    # False

# blank line to separate sections
print()

# test luhn_satisfied
print(luhn_satisfied("0"))                  # True
print(luhn_satisfied("4810024"))            # True
print(luhn_satisfied("4929004274674623"))   # True
print(luhn_satisfied(""))                   # False
print(luhn_satisfied("481o024"))            # False
print(luhn_satisfied("4810027"))            # False
print(luhn_satisfied("sloth"))              # False