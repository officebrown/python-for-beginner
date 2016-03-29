# Password
# Demonstrates the if statement

print("Welcome to System Security Inc.")
print("-- where security is our middle name\n")

created_password = input("Create a password: ").strip()
created_password2 = input("Create another password: ").strip()
password = input("Enter your password: ")

if password == created_password + created_password2:
    print("Access Granted")
#elif password == created_password2:
#	print("Access Granted")
else:
	print("Access Denied")

input("\n\nPress the enter key to exit.")
