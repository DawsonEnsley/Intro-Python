# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# print("Hello World!")
# name = input("What's your name?\n")
# print(f"Welcome to Pycharm, {name}!")
# import time
#
#
# def print_greeting():
#     your_name = input("Hello, what's your name?\n")
#     time.sleep(1)
#
#
# def answer():
#     print(f'Hello there!')
#     time.sleep(1)
#
#
# def goodbye():
#     print(f"It was nice to meet you, but I've gotta run. Goodbye!")
#     time.sleep(1)
#
#
# print_greeting()
# answer()
# goodbye()

# import time
# def print_pause(print_sleep):
#     print(print_sleep)
#     time.sleep(2)
#
#
# def valid_input(prompt, option1, option2):
#     while True:
#         response = input(prompt).lower()
#         if option1 in response:
#             break
#         elif option2 in response:
#             break
#         else:
#             print_pause("Sorry, I don't understand.")
#     return response
#
#
# def intro():
#     print_pause("Hello! I am Bob, the Breakfast Bot.")
#     print_pause("Today we have two breakfasts available.")
#     print_pause("The first is waffles with strawberries and whipped cream.")
#     print_pause("The second is sweet potato pancakes with butter and syrup.")
#
#
# def take_order():
#     response = valid_input("Please place your order. "
#                            "Would you like waffles or pancakes?\n",
#                            "waffles", "pancakes")
#     if "waffles" in response:
#         print_pause("Waffles it is!")
#     elif "pancakes" in response:
#         print_pause("Pancakes it is!")
#     print_pause("Your order will be ready shortly.")
#
#
# def another_order():
#     order_again = valid_input("Would you like to place another order?\n "
#                               "Please say 'yes' or 'no'.\n",
#                               "yes", "no")
#     if "no" in order_again:
#         print_pause("Okay, Goodbye!\n")
#     elif "yes" in order_again:
#         print_pause("Wonderful! I'm happy to take another order.\n")
#         take_order()
#
#
# def order_breakfast():
#     intro()
#     take_order()
#     another_order()
#
#
# order_breakfast()
import turtle
#   Create Name
# weaver = turtle.Turtle()
#   Draw Chain or Links
#   Create Variables
# links = [1, 2, 3, 4, 5, 6]
# sides = [1, 2, 3, 4, 5, 6]
#   Create Parameters
# weaver.width(5)
# weaver.color('orange')
#   Move back so the chain is centered.
# weaver.penup()
# weaver.back(80)
# weaver.pendown()
# Create Loop Expression
# for chain in links:
#   Draw a Hexagon
# for shape in sides:
#   weaver.forward(50)
#   weaver.right(60)
#   weaver.speed(5)
#   Scoot over to the next link.
# weaver.penup()
# weaver.forward(20)
# weaver.left(60)
# weaver.pendown()

#   Draw Line Skips
# lane = turtle.Turtle()
# lane.hideturtle()
#   Make the width thicker
# lane.width(5)
#   Move back without drawing
# lane.penup()
# lane.left(90)
# lane.forward(5)
# lane.right(90)
# lane.back(100)
# lane.pendown()
#   Draw a red line
# lane.color("red")
# lane.forward(50)
#   Move forward without drawing
# lane.penup()
# lane.forward(50)
# lane.pendown()
#   Draw an orange line
# lane.color("orange")
# lane.forward(50)
#   Move forward without drawing
# lane.penup()
# lane.forward(50)
# lane.pendown()
#   Draw a yellow line
# lane.color("yellow")
# lane.forward(50)

#   Draw Lines with Loop
# for lines in [1, 2, 3]:
#   lane.forward.(50)
#   lane.penup()
#   lane.forward(50)
#   lane.pendown()

#   Draw Lines with Change in color in For Loop
# for diff_color in ["red", "orange", "yellow"]:
#   lane.color(diff_color)

#   Draw Shape instead of Line with Nested Loop

# Lane = turtle.Turtle()
# Lane.hideturtle()
# Lane.width(5)
# Lane.penup()
# Lane.back(100)
# Lane.pendown()
# Lane.showturtle()

# for diff_color in ["green", "blue", "purple"]:
#    Lane.color(diff_color)
#    for square in [1, 2, 3, 4]:
#         Lane.forward(50)
#         Lane.right(90)
#     Lane.penup()
#     Lane.forward(100)
#     Lane.pendown()

# paul = turtle.Turtle()
# sides = [1, 2, 3, 4]
# paul.width(5)
# paul.penup()
# paul.right(90)
# paul.forward(50)
# paul.left(90)
# paul.back(25)
# paul.pendown()

# for large in sides:
#     paul.forward(100)
#     paul.right(90)
#     for small in sides:
#         paul.forward(10)
#         paul.right(90)

# stair = turtle.Turtle()
#
# stair.speed(5)
# stair.color("green")
# stair.width(3)
#
# for steps in range(15):
#     stair.forward(10)
#
#     if steps % 2 == 0:
#         stair.left(90)
#     else:
#         stair.right(90)

# import turtle
# t = turtle.Turtle()
# s = turtle.Turtle()
#
#
# def tri_spiral(length, turn, color):
#     t.color(color)
#     t.width(3)
#     t.speed(7)
#     for side in range(length):
#         t.forward(side * 10)
#         t.right(turn)
#
#
# tri_spiral(22, 120, "green")
#
#
# def spiral(sides, turn, color, width):
#     s.color(color)
#     s.width(width)
#     s.speed(7)
#     for n in range(sides):
#         s.forward(n)
#         s.right(turn)
#
#
# spiral(50, 30, "gold", 3)
#
#
# def star(color, sides, length, angles, distance):
#     galileo = turtle.Turtle()
#     galileo.color(color)  # colorful!
#     galileo.width(5)  # visible!
#     galileo.speed(0)  # fast!
#     galileo.penup()
#     galileo.left(angles)  # away from center
#     galileo.forward(distance)
#     galileo.pendown()  # start drawing
#     for side in range(sides):
#         galileo.forward(length)
#         galileo.left(720 / sides)
#     galileo.hideturtle()  # just the star
#
#
# for angle in [180, 135, 90, 45, 0]:
#     star("red", 5, 60, angle, 100)
#
# for angle in [180, 135, 90, 45, 0]:
#     star("blue", 5, 30, angle, 50)
#
# for angle in [180, 135, 90, 45, 0]:
#     star("white", 5, 15, angle, 25)
#
#
# turtle.exitonclick()
