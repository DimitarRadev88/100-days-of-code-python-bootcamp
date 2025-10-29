from turtle import Turtle
ROAD_WIDTH = 600
START_CROSSWALK_COORDINATES = (ROAD_WIDTH / -2, -265)
FINISH_CROSSWALK_COORDINATES = (ROAD_WIDTH / -2, 265)
FINISH_LINE_Y = 280
FONT = ("Courier", 14, "normal")

class Road(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.create_crosswalk(START_CROSSWALK_COORDINATES, ROAD_WIDTH)
        self.create_crosswalk(FINISH_CROSSWALK_COORDINATES, ROAD_WIDTH)
        self.write_finish_line()
        self.create_lanes()

    def create_crosswalk(self, position, width):
        self.penup()
        self.pensize(2)
        self.setposition(position[0], position[1])
        self.pendown()
        self.forward(width)

    def write_finish_line(self):
        self.penup()
        self.setposition(0, FINISH_LINE_Y - 20)
        self.write(f"FINISH", False, "center", FONT)

    def create_lanes(self):
        self.penup()
        self.pensize(10)
        self.setposition(START_CROSSWALK_COORDINATES[0], START_CROSSWALK_COORDINATES[1])
        while self.ycor() < FINISH_CROSSWALK_COORDINATES[1] - 40:
            self.penup()
            self.setposition(START_CROSSWALK_COORDINATES[0] + 20, self.ycor() + 41)
            for n in range(0, 600, 100):
                self.pendown()
                self.forward(50)
                self.penup()
                self.forward(50)

