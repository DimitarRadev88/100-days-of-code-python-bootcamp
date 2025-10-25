from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=1920, height=1080)
user_bet = screen.textinput("Make our bet", "Who will win the race? Enter a color")


def create_turtle(color):
    turtle = Turtle("turtle")
    turtle.shapesize(5)
    turtle.color(color)
    turtle.speed(5)
    turtle.penup()
    return turtle

purple_turtle = create_turtle("purple")
blue_turtle = create_turtle("blue")
green_turtle = create_turtle("green")
yellow_turtle = create_turtle("yellow")
orange_turtle = create_turtle("orange")
red_turtle = create_turtle("red")

turtles = [purple_turtle, blue_turtle, green_turtle, yellow_turtle, orange_turtle, red_turtle]

def align_on_start():
    y = 300
    for turtle in turtles:
        turtle.setposition(-900,y)
        y -= 100

def race():
    while True:
        for turtle in turtles:
            turtle.forward(randint(1, 20))
            if turtle.xcor() >= 900:
                return turtle

t = None
if user_bet:

    align_on_start()
    t = race()

if t.fillcolor() == user_bet:
    print("You've won!")
else:
    print("You've lost!")

print(f"The {t.pencolor()} turtle is the winner!")
screen.exitonclick()
