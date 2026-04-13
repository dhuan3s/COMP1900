# converts integers into their English pronunciation

# Problem 1
def one_digit_to_str(n):
    # list of words for digits 0-9
    digits = ["zero", "one", "two", "three", "four",
              "five", "six", "seven", "eight", "nine"]
    # return the word that matches the digit
    return digits[n]


# Problem 2
def two_digit_to_str(n):
    # uses first function if single digit
    if n < 10:
        return one_digit_to_str(n)

    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    # words for multiples of 10, zero omitted and 1's handled by teens
    tens_string = ["", "", "twenty", "thirty", "forty",
                  "fifty", "sixty", "seventy", "eighty", "ninety"]
    # check if number is in the teen range
    if 10 <= n < 20:
        return teens[n - 10]

    # split number into tens and ones places
    tens_value = n // 10
    ones = n % 10

    # if no ones digit, return the tens string
    if ones == 0:
        return tens_string[tens_value]  # return tens value word if under 100
    else: # otherwise combine tens and ones
        return tens_string[tens_value] + " " + one_digit_to_str(ones)

# Problem 3
def three_digit_to_str(n):
    if n < 100:     # if less than 100, reuse two_digit function
        return two_digit_to_str(n)

    # get hundreds place and remainder
    hundreds = n // 100
    remainder = n % 100

    #returns hundreds part of string if no remainer
    if remainder == 0:
        return one_digit_to_str(hundreds) + " hundred"
    else: # otherwise combines hundreds with rest of result
        return one_digit_to_str(hundreds) + " hundred " + two_digit_to_str(remainder)


# Problem 4
def int_to_str(n):
    if n == 0: # returns zero if input is 0
        return "zero"

    results = [] # list to store parts of the final phrase

    # get billions place
    billions = n // 1000000000
    n %= 1000000000

    # get millions place
    millions = n // 1000000
    n %= 1000000

    # get thousands place
    thousands = n // 1000
    n %= 1000 # remove thousands from n

    # converts billions and adds to list
    if billions > 0:
        results.append(three_digit_to_str(billions) + " billion")
    if millions > 0: # converts millions and adds to list
        results.append(three_digit_to_str(millions) + " million")
    if thousands > 0: # converts thousands and adds to list
        results.append(three_digit_to_str(thousands) + " thousand")
    if n > 0: # convert remaining art and adds to lsit
        results.append(three_digit_to_str(n))

    return " ".join(results).strip() # join phrase together using results list


# Problem 5
if __name__ == '__main__':
    while True: # User inputs integer into program
        num = int(input("Enter an integer to pronounce (0-999999999999, any negative value to exit):\n"))

        if num < 0: # Exit loop if negative num entered
            print("kthxbye!")
            break

        if num > 999999999999: # Makes sure input is valid and not too large
            print("Cannot be over 999999999999, try again:")
            continue

        print(int_to_str(num)) # Print the integer entered as words in string