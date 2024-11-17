# FILENAME = "text.txt"
# in_file = open(FILENAME)
# text = in_file.read() / text = in_file.readlines()
# in_file.close()
#
# print(text)
#
# FILENAME = "text.txt"
# in_file = open(FILENAME)
# for line in in_file:
#     print(line.strip())
# in_file.close()

# name = input("Name: ")
# out_file = open("name.txt", "a")
# print(name, file=out_file)
# out_file.close()

# countries = ["Italy", "England", "Finland", "Japan"]
#
# out_file = open("name.txt", "w")
# out_file.writelines(countries)
# out_file.close()

# name = input("Name: ")
# out_file = open("name.txt", "w")
# print(name, file=out_file)
# out_file.close()
# print("Done")
#
# name = input("Name: ")
# with open("name.txt", "w") as out_file:
#     print(out_file.read())
# print("Done")

# List of strings

# names = ["Alice", "Bob"]
#
# for name in names:
#     out_file = open(f"{name}.txt", "w")
#     print(name, file=out_file)
#     out_file.close()

# Method 1

# FILENAME = "data.txt"
# in_file = open(FILENAME)
# for line in in_file:
#     name = line.strip()
#     country = in_file.readline().strip()
#     print(f"{name} was born in {country}")
# in_file.close()

# Method 2

# FILENAME = "data.txt"
#
# with open(FILENAME, "r") as in_file:
#     lines = in_file.readlines()
#
# for i in range(0, len(lines), 2)
#     print(f"{lines[i]} was born in {lines[i+1]}")

# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Division cannot divide by zero")

# try:
#     in_file = open("abc.txt", "r")
#     text = in_file.read()
#
# except FileNotFoundError:
#     print("File not found")
#
# try:
#     number = int(input("Enter number: "))
#     print(number)
# except ValueError:
#     print("Input is not a number")
#
# try:
#     print(a + b)
# except TypeError:
#     print("Incorrect object type")

# age = 0
# valid_input = False
# while not valid_input:
#     try:
#         age = int(input("Age: "))
#         valid_input = True
#     except ValueError:
#         print("Invalid (not an integer)")
#     else:
#         print(f"Next year you will be {age + 1}")
#     finally:
#         print("Good try")

# def lbyl_convert_str_to_int(text):
#     """Look Before you leap version"""
#     if not isinstance(text, str) or not text.isdigit():
#         return None
#     else:
#         return int(text)
#
# def eafp_convert_str_to_int(text):
#     """Easier to ask forgiveness than permission version"""
#     try:
#         return int(text)
#     except ValueError:
#         return None

from math import pi
print(pi)














