# Counter
# Demonstrates the range() function
first = int(input("enter starting number:" ))
last = int(input("enter ending number:" ))
skip = int(input("enter number to count by:" ))


print("\n\nCounting by:")
for i in range(first, last, skip):
    print(i, end=" ")
i += skip
print(i)

input("\n\nPress the enter key to exit.\n")
