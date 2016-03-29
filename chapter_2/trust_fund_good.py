# Trust Fund Buddy - Good
# Demonstrates type conversion

print(
"""
                       Trust Fund Buddy

Totals your monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).

Please enter the requested, monthly costs.  Since you're rich, ignore pennies
and use only dollar amounts.

"""
)

car = input("Lamborghini Tune-Ups: ")
car = int(car)

rent = int(input("Manhattan Apartment: "))
jet = int(input("Private Jet Rental: "))
gifts = int(input("Gifts: "))
food = int(input("Dining Out: "))
staff = int(input("Staff (butlers, chef, driver, assistant): "))
guru = int(input("Personal Guru and Coach: "))
games = input("Computer Games: ")

total = car + rent + jet + gifts + food + staff + guru
total2 = games

print("\nGrand Total:", str(total) + total2)
print("\nGrand Total:", total + int(total2))

input("\n\nPress the enter key to exit.")


car = input("Lamborghini Tune-Ups: ")
rent = input("Manhattan Apartment: ")
jet = input("Private Jet Rental: ")
gifts = input("Gifts: ")
food = input("Dining Out: ")
staff = input("Staff (butlers, chef, driver, assistant): ")
guru = input("Personal Guru and Coach: ")
games = input("Computer Games: ")

total = int(car) + int(rent) + int(jet) + int(gifts) + int(food) + int(staff) + int(guru) + int(games)
total2 = car + rent + jet + gifts + food + staff + guru

print("\nGrand Total:", total)
print("\nGrand Total:", total2)

input("\n\nPress the enter key to exit.")
