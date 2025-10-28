from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.create()

    def create(self):
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0, 200)
        self.write(f"{self.p1_score}   {self.p2_score}", False, "center", ("Arial", 32, "bold"))

    def update_score(self):
        self.reset()
        self.create()
