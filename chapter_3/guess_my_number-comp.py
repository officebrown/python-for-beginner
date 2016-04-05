# Computer Guesses My Number
#
# The person picks a random number between 1 and 100
# The computer tries to guess it and the computer lets
# the person know if the guess is too high, too low
# or right on the money

import random


number_entered = int(input('enter a number: '))

tries = 1
guess = 0
low = 1
high = 100

while number_entered != guess:
	guess = random.randint(low,high)
	#print('computer guess: ', guess)
	if guess > number_entered:
		print("Computer guessed:",guess," but the number was lower")
		high = guess - 1
		tries += 1
	elif guess < number_entered:
		print("Computer guessed:",guess," but the number was higher")
		low = guess + 1
		tries += 1
	else:
		break

print("The number was", number_entered)
print("And it only took", tries, "tries!\n")

input("\n\nPress the enter key to exit.")
