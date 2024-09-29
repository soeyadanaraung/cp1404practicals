MINIMUM_LENGTH = 5
password = input("Enter a password: ")
while len(password) < MINIMUM_LENGTH:
    print("The password doesn't meet the minimum length")
    password = input("Enter a password: ")
print("*" * len(password))