from turtle import Turtle, Screen



def move_forward():
    donatello.forward(10)

def move_backward():
    donatello.backward(10)

def rotate_clockwise():
    donatello.left(5)

def rotate_counter_clockwise():
    donatello.right(5)

def add_event_listeners():
    screen.onkeypress(move_forward, "w")
    screen.onkeypress(move_backward, "s")
    screen.onkeypress(rotate_clockwise, "d")
    screen.onkeypress(rotate_counter_clockwise, "a")
    screen.onkeypress(screen.reset, "c")

donatello = Turtle("turtle")
donatello.speed("fastest")

screen = Screen()

add_event_listeners()
screen.listen()
screen.exitonclick()

