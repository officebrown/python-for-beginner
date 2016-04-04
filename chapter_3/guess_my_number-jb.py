# Random Number game.
import random

name = input('What is your name? ')
print(name.title().strip() + ', welcome to "Guess My Number", yo!')

number_picked = random.randint(1, 100)

guess = int(input('Guess the number: '))

tries = 1
while guess != number_picked:

	if guess > number_picked:
		guess = int(input('Try a lower number: '))

	else:
		guess = int(input('Try a higher number: '))

	tries += 1

	if tries == 3:
		print('loser')

		print('\nThe number was: ', number_picked)
		print(name, ", it took you", tries, "tries to fail.")
		break


print('\nThe number was: ', number_picked)
print(name, ", it took you", tries, "tries.")






input("\n\nPress the enter key to exit.")
