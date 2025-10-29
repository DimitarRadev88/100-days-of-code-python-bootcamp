from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 16
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.setheading(90)
        self.color("green")
        self.return_to_start()


    def is_at_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y

    def return_to_start(self):
        self.setposition(STARTING_POSITION[0], STARTING_POSITION[1])

    def jump(self):
        self.forward(MOVE_DISTANCE)
