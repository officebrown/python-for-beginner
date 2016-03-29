# Craps Roller
# Demonstrates random number generation

import random

# generate random numbers 1 - 6
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
die3 = random.randrange(6) + 1
die4 = random.randrange(6) + 1

total = die1 + die2
total2 = die3 + die4

print("You rolled a", die1, "and a", die2, "for a total of", total)
print("You rolled a", die3, "and a", die4, "for a total of", total2)

input("\n\nPress the enter key to exit.")
