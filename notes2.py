# Translating a for loop into a while loop example 1
# word = "cat"
# for index in range(len(word)):
#     print(word[index])
#
# index = 0
# word = "cat"
# while index < len(word):
#     print(word[index])
#     index += 1

# Translating a for loop into a while loop example 1
# def count_character(string, target):
#     total = 0
#     for ch in string:
#         if ch == target:
#             total += 1
#     return total
#
# # print(count_character("bonobo", "o"))
#
#
# def character_count(string, target):
#     index = 0
#     total = 0
#     while index < len(string):
#         if string[index] == target:
#             total += 1
#         index += 1
#     return total
#
#
# print(character_count("bonobo", "o"))

# def until_dot(a):
#     index = 0
#     while index < len(a) and a[index] != ".":
#         index += 1
#     return a[:index]
#
#
# print(until_dot("Udacity.com"))


# def is_substring(substring, string):
#     index = 0
#     while index < len(string):
#         if string[index : index + len(substring)] == substring:
#             return True
#         index += 1
#     return False

# Count Substrings
# def count_substring(string, target):
#     index = 0
#     total = 0
#     while index < len(string):
#         if string[index : index + len(target)] == target:
#             total += 1
#             index += len(target)
#         else:
#             index += 1
#     return total
#
# print(count_substring('love, love, love, all you need is love', 'love'))
# print(count_substring('ABBA', 'AB'))

# Locate First Substring
# def locate_first(string, sub):
#     index = 0
#     while index < len(string):
#         if string[index : index + len(sub)] == sub:
#             return index
#         else:
#             index += 1
#     return -1

# Locate all Substrings
# def locate_all(string, sub):
#     matches = []
#     index = 0
#     while index < len(string):
#         if string[index : index + len(sub)] == sub:
#             matches.append(index)
#             index += len(sub)
#         else:
#             index += 1
#     return matches

# Line breaks in a single string
# a = """apples
# oranges
# bananas
# grapes"""
# print(a)
#
# # Line breaks with join method
# lines = ["Haiku frogs in snow",
#          "A limerick came from Nantucket",
#          "Tetra drum-beats thrumming, Hawaii rhythm."]
#
# # Write your function definition here:
# def breaking(strings):
#     return "<br>".join(strings)
# print(breaking(lines))

# # Remove method inside of a string
# def remove_substring(string, sub):
#     output = []
#     index = 0
#     while index < len(string):
#         if string[index:index + len(sub)] == sub:
#             index += len(sub)
#         else:
#             output.append(string[index])
#             index += 1
#     return "".join(output)

# Test your function:
# print(remove_substring('SPAM!HelloSPAM! worldSPAM!!', 'SPAM!'))
# print(remove_substring("Whoever<br> wrote this<br> loves break<br> tags!", "<br>"))
# print(remove_substring('I am NOT learning to code.', 'NOT '))

# # Find and Replace in strings
# def replace_substring(string, substring, replacement):
#     output = []
#     index = 0
#     while index < len(string):
#         if string[index:index+len(substring)] == substring:
#             index += len(substring)
#         else:
#             output.append(replacement)
#             index += 1
#     return "".join(output)

# Test Examples:
# print(replace_substring('Hot SPAM!drop soup, and curry with SPAM!plant.', 'SPAM!', 'egg'))
# print(replace_substring("The word 'definitely' is definitely often misspelled.", 'definitely', 'definitely'))

# Exercise Example for Find and replace from detached lists
# nouns = [list of strings here]
# verbs = [list of strings here]
# templates = [
#         'Waiter! I found a {{noun}} in my {{noun}}!',
#         'The {{noun}} {{verb}} the {{noun}}.',
#         'If you {{verb}} the {{noun}}, '
#         'the {{noun}} will get you.',
#         "Let's go: the {{noun}} is {{verb}}.",
#         'Colorless green {{noun}}s {{verb}} furiously.']
#
# import random
#
# def silly_string(nouns, verbs, templates):
#     # Choose a random template.
#     template = random.choice(templates)
#     noun = random.choice(nouns)
#     verb = random.choice(verbs)
#     # We'll append strings into this list for output.
#     output = []
#     # Keep track of where in the template string we are.
#     index = 0
#     # Add a while loop here.
#     while index < len(template):
#         if template[index:index+8] == "{{noun}}":
#             output.append(noun)
#             index += 8
#         elif template[index:index+8] == "{{verb}}":
#             output.append(verb)
#             index += 8
#         else:
#             output.append(template[index])
#             index += 1
#     # After the loop has finished, join the output and return it.
#     output = "".join(output)
#     return output

# To see the results, we need to call the function and print what it returns:
# print(silly_string(nouns, verbs, templates))
