from turtle import Turtle

class Scoreboard(Turtle):



    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(0, 280)
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center")

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", False, align="center")

