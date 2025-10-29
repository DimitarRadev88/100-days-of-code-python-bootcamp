from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
CAR_LANES = [-224, -183, -142, -101, -60, -19, 22, 63, 104, 145, 186, 227, 268]


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_cars()
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_cars(self):
        for _ in range(0, 30):
            self.cars.append(self.create_car())

    def create_car(self):
        car = Turtle("square")
        car.color(choice(COLORS))
        car.shapesize(1, 2)
        car.penup()
        position = self.get_random_start_position()
        car.setposition(position[0], position[1])
        return car

    def get_random_start_position(self):
        car_lane = choice(CAR_LANES)
        return randint(-300, 1000), car_lane - 20

    def get_random_restart_position(self):
        car_lane = choice(CAR_LANES)
        return 320 + randint(100, 1000), car_lane - 20

    def move_cars(self):
        for car in self.cars:
            car.backward(self.move_distance)
            if car.xcor() < -320:
                new_position = self.get_random_restart_position()
                car.setposition(new_position[0], new_position[1])

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
