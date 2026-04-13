#Calculates what day of the week a given date is on using Zeller's Congruence formula

# List of days of week
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

#Collect date from user input
user_month = int(input("Enter the month (1-12): "))
q = int(input("Enter the day of the month (1-31): "))
user_year = int(input("Enter the year: "))

#Separate var must be created to treat jan and feb as diff year so they display properly for user
m = user_month
year = user_year

# Treat Jan and Feb as prev year
if m == 1 or m == 2:
    m += 12
    year -= 1

# Year of the century
k = year % 100

# Century
j = year // 100

#Zeller's Congruence
h = (q + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7

print(f"{user_month}/{q}/{user_year} is a {days[h]}.")