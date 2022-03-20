import time
items = []
# def word_pyramid(word):
#     length = len(word)
#     for n in range(length):
#         print(word[0:n + 1])
#
#
# word_pyramid("abracadabra")

# While Loops Example 1
# s = "Tenochtitlan"
# index = 0
# while index < len(s):
#     index -= 1
#     print(s[:index])

# def word_triangle(word):
#     length = len(word)
#     for n in range(length):
#         print(word[:length - n])
#
# word_triangle("abracadabra")

# While Loops Example 2
# s = "Abracadabra"
# index = len(s)
# while index > 0:
#     print(s[:index])
#     index -= 1
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

# Operations on Lists
# def total_length(list_of_strings):
#     total= 0
#     for string in list_of_strings:
#         total =total + len(string)
#     return total
#
# print(total_length(['foo', 'bar']))
# print(total_length([]))
# print(total_length(['balloons']))
# print(total_length(["", '', "", '']))

# import time
# n = 10
# while n > 0:
#     time.sleep(1)
#     print(n)
#     n -= 1
# print('Blastoff!')


def print_sleep(print_pause):
    print(print_pause)
    time.sleep(1)


def intro():
    print_sleep("You have just arrived at your new job!")
    print_sleep("You are in the elevator.")


def first_floor(items):
    print_sleep("You push the button for the first floor.")
    print_sleep("After a few moments, you find yourself in the Lobby.")
    if "ID card" in items:
        print_sleep("The clerk greets you, but she has already given you your"
                    " ID card, so there is nothing more to do here now.")
    else:
        print_sleep("The clerk greets you and gives you your ID card.")
        items.append("ID card")
    print_sleep("You head back to the elevator.")
    choose_floor(items)


def second_floor(items):
    print_sleep("You push the button for the second floor.")
    print_sleep("After a few moments, you find yourself in "
                "the human resources department.")
    if "handbook" in items:
        print_sleep("The HR folks are busy at their desks.")
        print_sleep("There doesn't seem to be much to do here.")
    else:
        print_sleep("The head of HR greets you.")
        if "ID card" in items:
            print_sleep("He looks at your ID card and then gives"
                        " you a copy of the employee handbook.")
            items.append("handbook")
        else:
            print_sleep("He has something for you, but says he can't "
                        "give it to you until you go get your ID card.")
    print_sleep("You head back to the elevator.")
    choose_floor(items)


def third_floor(items):
    print_sleep("You push the button for the third floor.")
    print_sleep("After a few moments, you find yourself in "
                "the engineering department.")
    print_sleep("This is where you work!")
    if "ID card" in items:
        print_sleep("You use your ID card to open the door.")
        print_sleep("Your program manager greets you and tells "
                    "you that you need to have a copy of the employee "
                    "handbook in order to start work.")
        if "handbook" in items:
            print_sleep("Fortunately, you got that from HR!")
            print_sleep("Congratulations! You are ready to start your new job"
                        " as vice president of engineering!")
        else:
            print_sleep("They scowl when they see that you don't have it, "
                        "and send you back to the elevator.")
            choose_floor(items)
    else:
        print_sleep("Unfortunately, the door is locked and you can't get in.")
        print_sleep("It looks like you need some kind of key card to open the door.")
        print_sleep("You head back to the elevator.")

    choose_floor(items)


def choose_floor(items):
    print_sleep("Please enter the number for the floor you would like to visit.")
    floor = input("1. Lobby\n"
                  "2. Human resources\n"
                  "3. Engineering department\n")
    if floor == '1':
        first_floor(items)
    elif floor == '2':
        second_floor(items)
    elif floor == '3':
        third_floor(items)


def play_game():
    items = []
    intro()
    choose_floor(items)


play_game()
