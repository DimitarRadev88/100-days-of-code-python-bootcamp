from turtle import Turtle


class Paddle:

    def __init__(self, side):
        super().__init__()
        self.parts = []
        self.side = side
        self.create()

    def create(self):
        for n in [40, 20, 0, -20, -40]:
            turtle = self.create_part()
            turtle.setposition(x=turtle.xcor(), y=n)
            self.parts.append(turtle)

    def create_part(self):
        turtle = Turtle()
        turtle.color("white")
        turtle.penup()
        turtle.shape("square")
        turtle.speed("fastest")
        turtle.setheading(90)
        if self.side == "left":
            turtle.setposition(x=-350, y=0)
        elif self.side == "right":
            turtle.setposition(x=350, y=0)

        return turtle

    def move_up(self):
        if self.parts[0].ycor() < 300:
            for part in self.parts:
                part.forward(20)

    def move_down(self):
        if self.parts[0].ycor() > -300:
            for part in self.parts:
                part.backward(20)
