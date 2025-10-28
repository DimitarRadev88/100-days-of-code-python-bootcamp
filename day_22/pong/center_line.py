from turtle import Turtle


class CenterLine(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.pensize(5)
        self.hideturtle()
        self.setheading(270)
        self.setposition(0, 310)
        for _ in range(16):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
