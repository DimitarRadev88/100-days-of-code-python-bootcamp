import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

window = Screen()
window.setup(width=640, height=640)
window.bgcolor("black")
window.title("Snake")
window.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
stop_game = False

def set_stop_game_true():
    global stop_game
    stop_game = True

window.onkey(snake.go_north, "Up")
window.onkey(snake.go_south, "Down")
window.onkey(snake.go_west, "Left")
window.onkey(snake.go_east, "Right")
window.onkey(set_stop_game_true, "Escape")
window.listen()


while not stop_game:
    window.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.grow()
        food.refresh()
        scoreboard.increase_score()

    if snake.has_hit():
        scoreboard.reset()
        scoreboard.write_score()
        snake.reset()

window.exitonclick()
