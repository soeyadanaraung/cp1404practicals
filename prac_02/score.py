import random

def main():
    score = int(input("Enter score: "))
    score_category = get_score_category(score)
    print(score_category)
    random_number = random.randint(1, 100)
    print(random_number)

def get_score_category(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"
random_number = random.randint(0,100)

main()

