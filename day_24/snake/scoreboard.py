from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as highscore:
            self.highscore = int(highscore.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setposition(0, 280)
        self.write_score()

    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align="center")

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write("GAME OVER", False, align="center")

    def reset(self):
        with open("data.txt", mode="w") as highscore:
            highscore.write(str(self.highscore))
        self.score = 0
