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

window.onkey(snake.go_north, "Up")
window.onkey(snake.go_south, "Down")
window.onkey(snake.go_west, "Left")
window.onkey(snake.go_east, "Right")
window.listen()

game_over = False

while not game_over:
    window.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.grow()
        food.refresh()
        scoreboard.increase_score()

    if snake.head.xcor() >= 320 or snake.head.xcor() <= -320 or snake.head.ycor() >= 320 or snake.head.ycor() <= -320:
        game_over = True

    for part in snake.snake_parts[1:]:
        if snake.head.distance(part) < 10:
            game_over = True

scoreboard.game_over()

window.exitonclick()
