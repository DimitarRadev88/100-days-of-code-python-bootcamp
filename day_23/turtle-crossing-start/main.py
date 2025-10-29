import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from road import Road
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
road = Road()
car_manager = CarManager()

screen.onkeypress(player.jump, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    for car in car_manager.cars:
        if car.ycor() - 20 <= player.ycor() <= car.ycor() + 20 and car.xcor() - 25 <= player.xcor() <= car.xcor() + 25:
            game_is_on = False
            scoreboard.game_over()
    if player.is_at_finish_line():
        scoreboard.update_level()
        player.return_to_start()
        car_manager.increase_speed()

screen.exitonclick()
