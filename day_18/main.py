from random import randint, choice
from turtle import Turtle, Screen


def goto_without_drawing(turtle, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_square(turtle, size):
    goto_without_drawing(turtle, size / -2, size / -2)

    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)


def draw_dashed_line(turtle, length):
    goto_without_drawing(turtle, length / -2, 0)
    distance = 0
    while distance < length:
        pen_down_distance = 20 if length - distance > 20 else length - distance
        turtle.forward(pen_down_distance)
        distance += pen_down_distance
        pen_up_distance = 10 if length - distance > 10 else length - distance
        turtle.penup()
        turtle.forward(pen_up_distance)
        distance += pen_up_distance
        turtle.pendown()


def draw_figure(turtle, angles, length):
    for n in range(angles):
        turtle.forward(length)
        turtle.right(360 / angles)
        turtle.forward(length)


def draw_figures(turtle, start_angles, end_angles, size):
    goto_without_drawing(turtle, 0, size * (end_angles - start_angles) / 2)
    for n in range(start_angles, end_angles + 1):
        turtle.pencolor(get_random_color())
        draw_figure(turtle, n, size)


def get_random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def reset_turtle(turtle):
    turtle.pensize(1)
    turtle.speed(1)


def random_walk(turtle, length, count):
    turtle.pensize(10)
    turtle.speed(10)
    for _ in range(count):
        turtle.pencolor(get_random_color())
        turtle.setheading(choice([0, 90, 180, 270]))
        turtle.forward(length)

    reset_turtle(turtle)


def draw_spirograph(turtle, circle_count, size):
    leonardo.speed(size)
    leonardo.pensize(3)
    for _ in range(circle_count):
        turtle.pencolor(get_random_color())
        turtle.right(360 / circle_count)
        turtle.circle(size)
    reset_turtle(turtle)


leonardo = Turtle(shape="turtle")
leonardo.color("green")
screen = Screen()
screen.colormode(255)

draw_spirograph(leonardo, 100, 200)

# draw_square(leonardo, 1000)
#
# draw_dashed_line(leonardo, 1000)
#
# draw_figures(leonardo, 3, 10, 100)
#
# random_walk(leonardo, 20, 1000)

screen.exitonclick()
