"""
Word Occurrences
Estimate: 15 minutes
Actual: 25 minutes
"""

COLOUR_TO_HEXADECIMAL = {"aliceblue": "#b0bf1a", "coral": "#ff7f50", "fawn": "#e5aa70", "ruby": "#e0115f",
                         "lavender": "#e6e6fa", "iris": "#5a4fcf", "indigo": "#4b0082", "ginger": "#b06500",
                         "heliotrope": "#df73ff", "jade": "#00a86b"}
colour = input("Please enter a colour: ").lower()
while colour != "":
    try:
        print(f"The colour {colour} is {COLOUR_TO_HEXADECIMAL[colour]}.")
    except KeyError:
        print("The colour entered is invalid, please try again.")
    colour = input("Please enter a colour: ").lower()