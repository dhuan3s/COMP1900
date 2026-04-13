runs = 35
x = 500
running_total = 0


while runs > 0:
    running_total += x
    x -= 15
    runs -= 1

print(f"The sum of the arithemetic sequence is {running_total}.")