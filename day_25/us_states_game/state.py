from turtle import Turtle


class State(Turtle):

    def __init__(self, data, text_color):
        super().__init__()
        self.hideturtle()
        self.color(text_color)
        self.penup()
        self.setposition(x=data.x.item(), y=data.y.item())
        self.write(data.state.item(), False, "center", ("Arial", 4, "normal"))
