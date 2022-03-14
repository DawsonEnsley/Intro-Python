# def word_pyramid(word):
#     length = len(word)
#     for n in range(length):
#         print(word[0:n + 1])
#
#
# word_pyramid("abracadabra")
#  Use in interactive Terminal
#
#
# def word_triangle(word):
#     length = len(word)
#     for n in range(length):
#         print(word[:length - n])
#
#
# word_triangle("abracadabra")
#  Use in interactive Terminal

# Concatenation Example
# name = input("What's your name?\n\n")
# print("\nHello, ", name, "! It's nice to meet you.\n")
# color = input("What's your favorite color?\n\n")
# print("\nWow!", "I love the color", color, "!")

# F-strings Example (No Concatenation)
# name = input("What's your name?\n\n")
# print(f"\nHi, {name}! It's very nice to meet you.\n")
# color = input("What's your favorite color?\n\n")
# print(f"\nAh, {color}, what a lovely color!")

# f-strings Example: Use of int in strings
# n1 = int(input("Enter a number: "))
# n2 = int(input("Enter another number: "))
# n3 = int(input("Enter a third number: "))
# sum = int(n1) + int(n2) + int(n3)
# print(f'{n1} + {n2} + {n3} = {sum}')

# starts-with Example: parameters
# def starts_with(s1, s2):
#     if s1[0] == s2[0]:
#         return True
#     if s1[0] != s2[0]:
#         return False

# print(starts_with("banana", "bread"))
#
# print(starts_with("zamboni", "kiwi"))

# starts_with Example: Length of a string
# def starts_with(long, short):
#     for position in range(len(short)):
#         if long[position] != short[position]:
#             return False
#     return True

# print(starts_with("apple", "app"))
#
# print(starts_with("manatee", "mango"))

# starts_with Example: Slicing
# def starts_with(long, short):
#     if long[0:len(short)] == short:
#         return True
#     else:
#         return False

# print(starts_with("apple", "app"))
#
# print(starts_with("manatee", "mango"))

# Boolean Example
# def good_length(n):
#     return len(n) < 7 or len(n) < 65
#
#
# print(good_length("apple"))
#
# print(good_length("hippopotamus"))
