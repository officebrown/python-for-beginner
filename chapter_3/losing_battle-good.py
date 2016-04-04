# Losing Battle
# Avoids the dreaded infinite loop
import random
print("Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheathes his sword for the last fight of his life.\n")

input("\nPress the enter key to see how your hero fared.\n")

health = 100
trolls = 0

while health > 0:
	#trolls = trolls + 1
	#health = health - damage
	trolls += 1
	damage1 = random.randint(1,10)
	damage2 = random.randint(1,10)
	health -= damage1 + damage2

	print("Your hero swings and defeats an evil troll, but takes", damage1, "and", damage2, "=", damage1 + damage2, "damage points.\n")

print("Your hero fought valiantly and defeated", trolls, "trolls.")
print("But alas, your hero is no more.")

input("\n\nPress the enter key to exit.")
