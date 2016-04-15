# Random Access
# Demonstrates string indexing

import random

word = input("input a word: ")
#print("The word is: ", word, "\n")

high = len(word)
low = -len(word)
#total = high + low

#random_number = random.randint(1,10)
#word_length = len(word)

print(word[0])

for i in range(10):
    position = random.randrange(low, high)
    print("word[", position, "]\t", word[position])

input("\n\nPress the enter key to exit.")
