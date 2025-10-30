from turtle import Turtle


class Snake:
    head = None

    def __init__(self):
        self.snake_parts = []
        self.create_parts()

    def create_parts(self):
        self.head = self.create_part()
        self.head.setposition(x=-10, y=-10)
        self.snake_parts.append(self.head)

        for _ in range(5):
            turtle = self.create_part()
            turtle.setposition(x=self.snake_parts[-1].xcor() - 20, y=self.snake_parts[-1].ycor())
            self.snake_parts.append(turtle)

    def create_part(self):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.penup()

        return turtle

    def grow(self):
        turtle = self.create_part()
        turtle.setposition(x=self.snake_parts[-1].xcor(), y=self.snake_parts[-1].ycor())
        self.snake_parts.append(turtle)

    def go_north(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def go_south(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def go_west(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def go_east(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move(self):

        for n in range(len(self.snake_parts) - 1, 0, -1):
            self.snake_parts[n].setposition(x=self.snake_parts[n - 1].xcor(), y=self.snake_parts[n - 1].ycor())

        self.head.forward(20)

    def reset(self):
        for part in self.snake_parts:
            part.hideturtle()
        self.snake_parts.clear()
        self.create_parts()

    def has_hit(self):
        for part in self.snake_parts[1:]:
            if self.head.distance(part) < 10:
                return True

        return self.head.xcor() >= 320 or self.head.xcor() <= -320 or self.head.ycor() >= 320 or self.head.ycor() <= -320