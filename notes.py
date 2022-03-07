
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

import turtle
t = turtle.Turtle()
t.color("green")
t.width(3)
t.speed(5)

for side in range(22):
    t.forward(side * 10)
    t.right(120)

def spiral(sides, turn, color, width):
    s = turtle.Turtle()
    s.color(color)
    s.width(width)
    s.speed(5)
    for n in range(sides):
        s.forward(n)
        s.right(turn)

spiral(50, 30, "gold", 3)

turtle.exitonclick()
