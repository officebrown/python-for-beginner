# Exclusive Network
# Demonstrates logical operators and compound conditions

print("\tExclusive Computer Network")
print("\t\tMembers only!\n")

security = 0

username = ""
while not username:
    username = input("Username: ")

password = ""
while not password:
    password = input("Password: ")

if username == "M.Dawson" and password == "secret":
    security = 5
    print("Hi, Mike. Your security level is: ", security)
elif username == "S.Meier" and password == "civilization":
    security = 4
    print("Hey, Sid. Your security level is: ", security)
elif username == "S.Miyamoto" and password == "mariobros":
    security = 3
    print("What's up, Shigeru? Your security level is: ", security)
elif username == "W.Wright" and password == "thesims":
    security = 2
    print("How goes it, Will? Your security level is: ", security)
elif username == "guest" or password == "guest":
	security = 1
    print("Welcome, guest. Your security level is: ", security)
else:
    print("Login failed.  You're not so exclusive.\n")

input("\n\nPress the enter key to exit.")
