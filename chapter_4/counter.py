# Counter
# Demonstrates the range() function
first = 0
last = 500
skip = 5

print("Counting:")
for i in range(1000):
    print(i, end=" ")

print("\n\nCounting by fives:")
for i in range(first, last, skip):
    print(i, end=" ")
i += 5
print(i)

print("\n\nCounting backwards:")
for i in range(10, 0, -1):
    print(i, end=" ")

input("\n\nPress the enter key to exit.\n")
