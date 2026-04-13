print("You stand in the presence of the Magnificent Magic Mademoiselle Millicent. "
      "Prepare to be amazed!")
num = int(input("Enter an integer: "))

print("\nOK, watch this...")
newnum = num * 3
print(f"We'll multiply by 3 to get {newnum}.")
newnum += 15
print(f"Then we'll add 15 and get {newnum}.")
newnum = int(newnum/3)
print(f"Then we'll divide by 3 and get {newnum}.")
newnum -= num
print(f"Then we'll subtract the original number and get... {newnum}. Amazing!")