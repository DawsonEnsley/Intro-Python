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

import time

# items = []
#
# def print_sleep(print_pause):
#     print(print_pause)
#     time.sleep(1)
#
#
# def intro():
#     print_sleep("You have just arrived at your new job!")
#     print_sleep("You are in the elevator.")
#
#
# def first_floor(items):
#     print_sleep("You push the button for the first floor.")
#     print_sleep("After a few moments, you find yourself in the Lobby.")
#     if "ID card" in items:
#         print_sleep("The clerk greets you, but she has already given you your"
#                     " ID card, so there is nothing more to do here now.")
#     else:
#         print_sleep("The clerk greets you and gives you your ID card.")
#         items.append("ID card")
#     print_sleep("You head back to the elevator.")
#     choose_floor(items)
#
#
# def second_floor(items):
#     print_sleep("You push the button for the second floor.")
#     print_sleep("After a few moments, you find yourself in "
#                 "the human resources department.")
#     if "handbook" in items:
#         print_sleep("The HR folks are busy at their desks.")
#         print_sleep("There doesn't seem to be much to do here.")
#     else:
#         print_sleep("The head of HR greets you.")
#         if "ID card" in items:
#             print_sleep("He looks at your ID card and then gives"
#                         " you a copy of the employee handbook.")
#             items.append("handbook")
#         else:
#             print_sleep("He has something for you, but says he can't "
#                         "give it to you until you go get your ID card.")
#     print_sleep("You head back to the elevator.")
#     choose_floor(items)
#
#
# def third_floor(items):
#     print_sleep("You push the button for the third floor.")
#     print_sleep("After a few moments, you find yourself in "
#                 "the engineering department.")
#     print_sleep("This is where you work!")
#     if "ID card" in items:
#         print_sleep("You use your ID card to open the door.")
#         print_sleep("Your program manager greets you and tells "
#                     "you that you need to have a copy of the employee "
#                     "handbook in order to start work.")
#         if "handbook" in items:
#             print_sleep("Fortunately, you got that from HR!")
#             print_sleep("Congratulations! You are ready to start your new job"
#                         " as vice president of engineering!")
#         else:
#             print_sleep("They scowl when they see that you don't have it, "
#                         "and send you back to the elevator.")
#             choose_floor(items)
#     else:
#         print_sleep("Unfortunately, the door is locked and you can't get in.")
#         print_sleep("It looks like you need some kind of key card to open the door.")
#         print_sleep("You head back to the elevator.")
#
#     choose_floor(items)
#
#
# def choose_floor(items):
#     print_sleep("Please enter the number for the floor you would like to visit.")
#     floor = input("1. Lobby\n"
#                   "2. Human resources\n"
#                   "3. Engineering department\n")
#     if floor == '1':
#         first_floor(items)
#     elif floor == '2':
#         second_floor(items)
#     elif floor == '3':
#         third_floor(items)
#
#
# def play_game():
#     items = []
#     intro()
#     choose_floor(items)
#
#
# play_game()

import string

# rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]
#
#
# def check_line(line):
#     rude_count = 0
#     # We'll need the position of the current word in the list
#     word_index = 0
#     words = line.split(" ")
#     for word in words:
#         # We need to check stripped words separately now
#         stripped_word = word.strip(string.punctuation).lower()
#         if stripped_word in rude_words:
#             rude_count += 1
#             print(f"Found rude word: {word}")
#             # Find the current word in the words list and replace it
#             # with a bleeped version. Notice we use word rather than
#             # stripped_word, in order to keep the punctuation.
#             words[word_index] = bleeper(word)
#
#         word_index += 1 # Moving on to the next word
#     line = " ".join(words)
#     # We now return both the count and the line itself,
#     # so we can write the line to a file
#     return line, rude_count
#
#
# def check_file(filename):
#     with open(filename) as myfile:
#         rude_count = 0
#         # If the file has multiple lines, we will need
#         # to collect them all for the final output
#         lines = []
#         for line in myfile:
#             # Get the (potentially bleeped) line and
#             # the number of rude words in that line
#             line, rude_subtotal = check_line(line)
#             # Add to the total rude lines found in the file
#             rude_count += rude_subtotal
#             # Add the current line to the lines list
#             lines.append(line)
#
#     if rude_count == 0:
#         print("Congratulations, your file has no rude words.")
#         print("At least, no rude words I know.")
#     else:
#         # If rude words were found, write them to a new file
#         # and inform the user.
#         with open("bleeped_copy.txt", "w") as bleeped_copy:
#             bleeped_copy.write("\n".join(lines))
#         print(f"Found {rude_count} rude words in your file."
#               f" See bleeped_copy.txt for a censored copy of your file.")
#
# def bleeper(word):
#     pos = 0 # Track the position (index) of the character so we can replace it
#     for character in word:
#         if character not in string.punctuation:
#             character = "*" # If it wasn't punctuation, replace it
#         word = word.replace(word[pos], character) # Replace the character at the current position
#         pos += 1 # Move to the next character position
#     return word
#
#
# if __name__ == '__main__':
#     check_file("my_story.txt")

import requests

# try:
#     r = requests.get("https://www.udacity.com")
# except NameError:
#     print("Did you forget to import the requests module?")
#
# try:
#     print(r.text)
# except NameError:
#     print("There seems to be a NameError; r is not defined!")
#
# string = 'short'
# try:
#     for letter in range(6):
#         print(string[letter])
# except IndexError:
#     print("Did you try to index past the end of the string?")
#
# print("Woohoo! You got them all!")
#
# try:
#     r = requests.get("https://www.udacity.com")
#     print(r)
# except requests.exceptions.ConnectionError:
#     print("Could not connect to server.")

# weather = [
#     {
#         'date': 'today',
#         'state': 'cloudy',
#         'temp': 68.5
#     },
#     {
#         'date': 'tomorrow',
#         'state': 'sunny',
#         'temp': 74.8
#     }
# ]
#
# for e in weather:
#     print(e)
#
# for key in weather[0].keys():
#     print(key)
# print("Keys")
# for value in weather[0].values():
#     print(value)
# print("Values")
# for key, value in weather[0].items():
#     print(key)
#     print(value)
# print("Both")

# Simple Weather Report Example
# weather = [
#     {
#         'date':'today',
#         'state': 'cloudy',
#         'temp': 68.5
#     },
#     {
#         'date':'tomorrow',
#         'state': 'sunny',
#         'temp': 74.8
#     }
# ]

# for forecast in weather:
#     date = forecast['date']
#     state = forecast['state']
#     temp = forecast['temp']
#     print(f"The weather for {date} will be {state} with a temperature of {temp} degrees.")
#
# import requests
# r = requests.get('https://www.metaweather.com/api/location/2455920')
# d = r.json()
# for key in d:
#     print(key)

# d['consolidated_weather'][0]['max_temp']
# d['consolidated_weather'][0]['max_temp'] * 9/5 + 32
#
# for forecast in d['consolidated_weather']:
#     date = forecast['applicable_date']
#     humidity = forecast['humidity']
#     print(f"{date}\tHumidity: {humidity}")

# import requests
# Weather Application using Web APIs

# API_ROOT = 'https://www.metaweather.com'
# API_LOCATION = '/api/location/search/?query='
# API_WEATHER = '/api/location/'  # + woeid
#
# def fetch_location(query):
#     return requests.get(API_ROOT + API_LOCATION + query).json()
#
# def fetch_weather(woeid):
#     return requests.get(API_ROOT + API_WEATHER + str(woeid)).json()
#
# def disambiguate_locations(locations):
#     print("Ambiguous location! Did you mean:")
#     for loc in locations:
#         print(f"\t* {loc['title']}")
#
# def display_weather(weather):
#     print(f"Weather for {weather['title']}:")
#     for entry in weather['consolidated_weather']:
#         date = entry['applicable_date']
#         high = entry['max_temp']
#         low = entry['min_temp']
#         state = entry['weather_state_name']
#         print(f"{date}\t{state}\thigh {high:2.1f}°C\tlow {low:2.1f}°C")
#
# def weather_dialog():
#     try:
#         where = ''
#         while not where:
#             where = input("Where in the world are you? ")
#         locations = fetch_location(where)
#         if len(locations) == 0:
#             print("I don't know where that is.")
#         elif len(locations) > 1:
#             disambiguate_locations(locations)
#         else:
#             woeid = locations[0]['woeid']
#             display_weather(fetch_weather(woeid))
#     except requests.exceptions.ConnectionError:
#         print("Couldn't connect to server! Is the network up?")
#
# if __name__ == '__main__':
#     while True:
#         weather_dialog()
