colour = input("Please enter a colour: ").lower()
while colour != "":
    try:
        print(f"The colour {colour} is {COLOUR_TO_HEXADECIMAL[colour]}.")
    except KeyError:
        print("The colour entered is invalid, please try again.")
    colour = input("Please enter a colour: ").lower()