# total = 0
# count = 0
# age = int(input("Enter age; "))
# while age >= 0:
#     total += age
#     count += 1
#     age = int(input("Enter age: "))
# print("Total: ", total)
# print("Average age: ", total/count)

"""
get number of gifts
get number of students
display number of gifts // number of students
display number of gifts % number of students
"""

# number_of_gifts = int(input("Enter the number of gifts: "))
# number_of_students = int(input("Enter the number of students: "))
#
# gift_per_student = number_of_gifts // number_of_students
# gifts_left = number_of_gifts % number_of_students

# print(f"The number of gifts each student gets {gift_per_student}")
# print(f"Gift left over {gifts_left}")

# int = whole number 11
# float = any number with decimal point 11.5
# string = ... "11"
# bool = True and False
# list = allow to store many elements names = ["Small", "Medium", "Large"]
# normal variable: name = "Small"

# SG_GST = 0.09
# item_price = float(input("Enter the item price: "))
# tax_confirmation = input("Does your item include tax, Yes or No?: ").strip().upper()
#
# if tax_confirmation == "YES":
#     final_price = (item_price * SG_GST) + item_price
#     print(f"Final price is ${final_price: .2f}.")
# else:
#     print(f"Final price is ${item_price: .2f}.")

# 1) while loop
#
# number = int(input("Enter a number: "))
# count = 0
#
# while number > count:
#     count += 1
#     print(count)

# 2) for loop

# number = int(input("Enter a number: "))
#
# for i in range(1, number + 1):
#     print(i)

# SECRET_NUMBER = 7
#
# user_number = int(input("Guess a secret between 1 and 10: "))
#
# while user_number < 1 or user_number > 10:
#     print("Invalid input. Guess again.")
#     user_number = int(input("Guess a secret between 1 and 10: "))
#
# while user_number != SECRET_NUMBER:
#     print("Incorrect! Try again.")
#     user_number = int(input("Guess a secret between 1 and 10: "))
#
# print("Correct! Congratulations.")

# user_name = input("Enter your name: ").upper()
#
# while user_name == "":
#     print("User name can't be blank.")
#     user_name = input("Enter your name: ").upper()
#
# user_salary = float(input("Enter your salary: "))
#
# while user_salary < 0:
#     print("Salary must be greater than 0.")
#     user_salary = float(input("Enter your salary: "))
#
# print(f"{user_name}'s salary is ${user_salary}.")

# total_age = 0
# count = 0
# number_of_people = int(input("Number of people to enter: "))
#
# for i in range(1, number_of_people + 1):
#     age = int(input(f"Enter age for person {i}: "))
#     total_age += age
#     count += 1
#
# print(f"The total age is {total_age}.")
# print(f"The average age is {(total_age/count): .2f}.")

# total_age = 0
# count = 0
# age = int(input("Enter the age: "))
#
# while age != -1:
#     total_age += age
#     count += 1
#     age = int(input("Enter the age: "))
#
# average = total_age / count
# print(f"Total age is {total_age}.")
# print(f"Average age is {average}.")

# Guess the output
#
# for i in range(1, 4):
#     for j in range(2, 10, 3):
#         print(i, "-", j+i)

# 1-3
# 1-6
# 1-10
# 2-4
# 2-7
# 2-10
# 3-5
# 3-8
# 3-11
















