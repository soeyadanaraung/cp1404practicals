# names = ["Ada", "Alan", "Bill", "John"]
# print(", ". join(names))
# name_to_remove = input("Enter a name to remove: ")
#
# while name_to_remove != "":
#     if name_to_remove in names:
#         names.remove(name_to_remove)
#         print(", ". join(names))
#     else:
#         try:
#             names.remove(name_to_remove)
#             print(", ". join(names))
#         except ValueError:
#             print(f"{name_to_remove} is not in the list")
#             name_to_remove = input("Enter a name to remove: ")
#
# print("Final list of name is ",",".join(names))
from msvcrt import open_osfhandle

# def main():
#     numbers = [1, 2, 3]
#     add_offset(numbers, 2)
#     print(numbers)
#
# def add_offset(elem`  ents, offset):
#     for i in range(len(elements)):
#         elements[i] += offset
#
# main()

things = [True, 1.2, "Good", [1, 10]]

# print(things[-2])
# print("%".join([things[2][1:-1]]))
# print([str(t)[0] for t in things])
# print(([len(str(t)) for t in things]))
# print([t for t in things if type(t) in (float, int)])
# print([t for t in things if isinstance(t, int)])
#
# Good
# [oo]
# ['T', '1', 'G', '[']
# ["4", "3", "4", "7"]
# [1.2]
# [True]

# values = [[3, 4, 5, 1], [33, 6, 1, 2]]
#
# v = values[0][0]
# for row in range(0, len(values)):
# 	for column in range(0, len(values[row])):
# 		if v < values[row][column]:
# 			v = values[row][column]
#
# print(v)
#
# 33

# def main():
#     numbers = get_numbers()
#     square_numbers(numbers)
#     numbers.sort()  # Sort the squared numbers in ascending order
#     display_numbers(numbers)
#
# def get_numbers():
#     # Get input from the user and split it by commas to create a list of floats
#     user_input = input("Enter numbers separated by commas: ")
#     numbers = [float(num) for num in user_input.split(",")]
#     return numbers
#
# def square_numbers(numbers):
#     # Square each number in the list
#     for i in range(len(numbers)):
#         numbers[i] = numbers[i] ** 2
#
# def display_numbers(numbers):
#     # Display the squared and sorted numbers, separated by commas
#     print(", ".join([str(num) for num in numbers]))
#
# # Call the main function to run the program
# main()

# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
#
# Desired output from any similar list of [name, score] pairs:
#
# Derek       =   7
# Xavier      =  80
# Bob         = 612
# Chantanelle =   9

# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
#
# for name, score in data:
#     print(f"{name:<11} = {score:>3}")
#
# name_width = max((len(pair[0]) for pair in data))
# score_width = max((len(str(pair[1])) for pair in data))
#
# for pair in data:
#     name, score = pair
#     print(f"{name:{name_width}} = {score:{score_width}}")
# print()

things = list("one two three")
print("{}-{}".format(*things))
print(things)
string = ["one two three"]
print(string)

# before = [1, 4, 0, -1]
# before.sort()
# after = before
# print(after)