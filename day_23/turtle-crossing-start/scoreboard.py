from turtle import Turtle

FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.update_level()

    def update_level(self):
        self.reset()
        self.color("white")
        self.level += 1
        self.penup()
        self.hideturtle()
        self.setposition(-200, 220)
        self.write(f"Level: {self.level}", False, "center", FONT)

    def game_over(self):
        self.setposition(0, 20)
        self.write("GAME OVER", False, "center", FONT)
