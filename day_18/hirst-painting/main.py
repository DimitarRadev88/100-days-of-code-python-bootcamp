# import colorgram
from random import choice
from turtle import Turtle, Screen

# extract = colorgram.extract("image.jpg", 30)
#
# colors = []
#
# for color in extract:
#     colors.append((color.rgb[0], color.rgb[1], color.rgb[2]))
#
# print(colors)

colors = [
    (249, 248, 241), (250, 244, 248), (242, 250, 246), (242, 246, 251), (231, 224, 88),
    (227, 55, 126), (209, 162, 106), (110, 177, 210), (188, 77, 25), (191, 162, 23),
    (186, 42, 112), (39, 101, 159), (208, 138, 175), (47, 182, 113), (18, 28, 63),
    (25, 35, 156), (171, 18, 65), (230, 224, 8), (128, 188, 164), (229, 168, 197),
    (29, 175, 203), (50, 126, 79), (17, 49, 33), (55, 21, 31), (145, 216, 200),
    (231, 68, 38), (63, 28, 16), (136, 217, 228), (108, 94, 205), (156, 27, 17)
]

screen = Screen()

screen.colormode(255)

hirst = Turtle()
hirst.penup()

def create_dot_art(turtle, dots, size):
    def go_to_next_row():
        turtle.setheading(90)
        turtle.forward(size * 2)
        turtle.setheading(180)
        turtle.forward(int(size * dots / 10 * 2))
        turtle.setheading(0)

    turtle.speed("fastest")
    turtle.goto((dots * size / -10), (dots * size / -10))

    for y in range(0, int(dots / 10)):
        for x in range(0, int(dots / 10)):
            turtle.forward(size * 2)
            turtle.dot(size, choice(colors))
        go_to_next_row()


create_dot_art(hirst, 100, 50)

screen.exitonclick()
