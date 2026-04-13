import random

n = int(input("Slotherius uses Triple Claw Slash! How many seconds "
              "would you like to charge?"))
attackrand1 = random.randint(9, 16)
attackrand2 = random.randint(9, 16)

if n == 0:
    attack_sec = 15
elif n != 0:
    attack_sec = random.randint((15 - 7 * n), (15 + 8 * n))

print(f"\nDamage dealt:\nAttack 1: {attackrand1}\nAttack 2: {attackrand2}\nAttack 3: {attack_sec}")
if attack_sec < 0:
    print("\nOh no! Slotherius hurt himself in his confusion!")
