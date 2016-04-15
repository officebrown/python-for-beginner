# Message Analyzer
# Demonstrates the len() function and the in operator

# variables
message = input("Enter a message: ")
count = 0
e_count = 0
message_length = len(message)
e = "e"

print("\nThe length of your message is:", message_length)

# for loop that prints the message number of times equal to it's length and creates a count that doubles the message length
for i in range(message_length):
	print(message)
	count += 2

# variable that holds the value of the message length * count
value = (message_length * count)

print(value)

# checks to see if character count is correct by matching character length using value variable
if value == 338:
	print("your character count is correct")
else:
	print("your character count is incorrect")

print(message_length)

# checks to see if spelling is correct by matching character length using character length
if message_length == 13:
	print("your spelling is correct")
else:
	print("your spelling is incorrect")

print("\nThe most common letter in the English language, 'e', ")

if "e" in message:
	print("is in your message.")
else:
    print("is not in your message.")

input("\n\nPress the enter key to exit.")
