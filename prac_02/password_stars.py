def main():

    password = input("Enter a password: ")
    password = get_password(password)
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password(password):
    while len(password) < 5:
        print("The password doesn't meet the minimum length")
        password = input("Enter a password: ")
    return password


main()