# Lab HW 6 - Saying Numbers

# Problem 1
def one_digit_to_str(n):
    digits = ["zero", "one", "two", "three", "four",
              "five", "six", "seven", "eight", "nine"]
    return digits[n]


# Problem 2
def two_digit_to_str(n):
    if n < 10:
        return one_digit_to_str(n)

    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    tens_words = ["", "", "twenty", "thirty", "forty",
                  "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 10 <= n < 20:
        return teens[n - 10]

    tens = n // 10
    ones = n % 10

    if ones == 0:
        return tens_words[tens]
    else:
        return tens_words[tens] + " " + one_digit_to_str(ones)


# Problem 3
def three_digit_to_str(n):
    if n < 100:
        return two_digit_to_str(n)

    hundreds = n // 100
    remainder = n % 100

    if remainder == 0:
        return one_digit_to_str(hundreds) + " hundred"
    else:
        return one_digit_to_str(hundreds) + " hundred " + two_digit_to_str(remainder)


# Problem 4
def int_to_str(n):
    if n == 0:
        return "zero"

    parts = []

    billions = n // 1_000_000_000
    n %= 1_000_000_000

    millions = n // 1_000_000
    n %= 1_000_000

    thousands = n // 1_000
    n %= 1_000

    if billions > 0:
        parts.append(three_digit_to_str(billions) + " billion")
    if millions > 0:
        parts.append(three_digit_to_str(millions) + " million")
    if thousands > 0:
        parts.append(three_digit_to_str(thousands) + " thousand")
    if n > 0:
        parts.append(three_digit_to_str(n))

    return " ".join(parts).strip()


# Problem 5
if __name__ == '__main__':
    while True:
        num = int(input("Enter an integer to pronounce (0-999999999999, any negative value to exit):\n"))
