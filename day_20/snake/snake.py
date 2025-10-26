from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_parts()

    def create_parts(self):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()

        self.snake_parts = [turtle]
        for _ in range(5):
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.setposition(x=self.snake_parts[-1].xcor() - 20, y=self.snake_parts[-1].ycor())
            self.snake_parts.append(turtle)

    def grow(self):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()
        turtle.setposition(x=self.snake_parts[0].xcor(), y=self.snake_parts[0].ycor())
        turtle.forward(20)
        self.snake_parts.insert(0, turtle)
        self.snake_parts[0].forward(20)

    def go_north(self):
        if self.snake_parts[0].heading() != 270:
            self.snake_parts[0].setheading(90)

    def go_south(self):
        if self.snake_parts[0].heading() != 90:
            self.snake_parts[0].setheading(270)

    def go_west(self):
        if self.snake_parts[0].heading() != 0:
            self.snake_parts[0].setheading(180)

    def go_east(self):
        if self.snake_parts[0].heading() != 180:
            self.snake_parts[0].setheading(0)

    def move(self):
        for n in range(len(self.snake_parts) - 1, 0, -1):
            self.snake_parts[n].setposition(x=self.snake_parts[n - 1].xcor(), y=self.snake_parts[n - 1].ycor())

        self.snake_parts[0].forward(20)
