import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

def main():
    number_of_picks = int(input("How many quick picks? "))

    generate_quick_picks(number_of_picks)

def generate_quick_picks(number_of_picks):
    for i in range(number_of_picks):
        quick_pick = []
        while len(quick_pick) < NUMBERS_PER_LINE:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
            if number not in quick_pick:
                quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{num:2}" for num in quick_pick))


main()