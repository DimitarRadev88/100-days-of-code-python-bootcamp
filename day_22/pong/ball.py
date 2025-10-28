from random import randint
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.possession = "left"
        self.create()

    def create(self):
        self.color("white")
        self.shape("circle")
        self.speed(randint(5, 10))
        self.penup()
        angle = 0
        if self.possession == "left":
            angle = 360 - randint(0, 60)
            self.possession = "right"
        elif self.possession == "right":
            angle = 180 + randint(0, 60)
            self.possession = "left"
        self.setheading(angle)

    def move(self):
        self.forward(1)

    def has_hit_wall(self):
        return self.ycor() >= 300 or self.ycor() <= -300

    def bounce(self):
        self.setheading(360 - self.heading())
        self.tilt(self.heading() * -1)
        self.forward(2)

    def is_out_of_field(self):
        return self.xcor() < -600 or self.xcor() > 600

    def hit_paddle(self):
        if self.heading() <= 90:
            self.setheading(randint(120, 180))
        elif self.heading() <= 180:
            self.setheading(randint(0, 60))
        elif self.heading() <= 270:
            self.setheading(randint(300, 360))
        else:
            self.setheading(randint(180, 240))

        self.forward(2)
        self.speed(randint(5, 10))
