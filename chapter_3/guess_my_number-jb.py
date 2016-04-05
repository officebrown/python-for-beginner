# Random Number game.
import random

name = input('What is your name? ')
print(name.title().strip() + ', welcome to "Guess My Number", yo!')

number_picked = random.randint(1, 100)

guess = int(input('Guess the number: '))

tries = 1

while guess != number_picked and tries < 3:

	if guess > number_picked:
		guess = int(input('Try a lower number: '))

	elif guess < number_picked:
		guess = int(input('Try a higher number: '))

	tries += 1

if tries == 3:

	print('LOSER! \nThe number was: ', number_picked)
	print("and it took you", tries, "tries to fail.")

else:

	print('\nThe number was: ', number_picked)
	print("and it took you", tries, "tries.")
