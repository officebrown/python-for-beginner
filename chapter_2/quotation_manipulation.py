# Quotation Manipulation
# Demonstrates string methods

# quote from IBM Chairman, Thomas Watson, in 1943
quote = "I think there is a big world"
quote2 = " market for maybe five big computers."
quote3 = "I think there is a big world market for maybe five big computers."

print("Original quote:")
print(quote + quote2)

print("\nIn uppercase:")
print(quote.upper() + quote2.upper())

print("\nIn lowercase:")
print(quote.lower() + quote2.lower())

print("\nIn uppercase/lower:")
print(quote.upper() + quote2.lower())

print("\nAs a title:")
print(quote.title() + quote2.title())

print("\nWith a minor replacement:")
print(quote3.replace("big", "small", 1))

print("\nWith a strip():")
print(quote + quote2.strip())

print("\nWith a swapcase():")
print(quote3.swapcase())

print("\nWith a minor replacement: * 10")
print((quote + quote2.replace("five", "millions of") + "\n") * 10)

input("\n\nPress the enter key to exit.")
