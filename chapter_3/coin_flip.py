# flips a coin 100 times and tells the number of heads and tails

import random



#result = random.randint(1,2)

#heads = 1
#tails = 2

total_heads = 0
total_tails = 0
number_flips = 0

while number_flips < 100:
	result = random.randint(1,2)
	if result == 1:
		#print('heads')
		total_heads += 1
		number_flips += 1

	else:
		#print('tails')
		total_tails += 1
		number_flips += 1


print("total flips =", number_flips)
print("total heads =", total_heads)
print("total tails =", total_tails)
