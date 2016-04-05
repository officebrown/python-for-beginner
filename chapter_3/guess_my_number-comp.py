# Computer Guesses My Number
#
# The person picks a random number between 1 and 100
# The computer tries to guess it and the computer lets
# the person know if the guess is too high, too low
# or right on the money

import random


number_entered = int(input('enter a number: '))


tries = 1
guess = random.randint(1, 100)
new_guess = 0

while number_entered != guess or new_guess:
	if guess or new_guess > number_entered:
		print("Lower...")
		new_guess = random.randint(1, 100)
		print(new_guess)

	else:
		print("Higher...")
		new_guess = random.randint(1, 100)
		print(new_guess)

	tries += 1




print(guess)
print(new_guess)
print("You guessed it!  The number was", number_entered)
print("And it only took you", tries, "tries!\n")

input("\n\nPress the enter key to exit.")
