import csv
from guitar import Guitar

def main():
    guitars =  load_file()
    display_guitars(guitars)

def display_guitars(guitars):
    for guitar in guitars:
        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost: .2f}")

def load_file():
    guitars = []
    with open("guitars.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            guitars.append(Guitar(row[0], int(row[1]), float(row[2])))
    return guitars

if __name__ == '__main__':
    main()