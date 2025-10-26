import time
from turtle import Screen, Turtle

from snake import Snake

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake")
window.tracer(0)

snake = Snake()

window.onkey(snake.go_north, "Up")
window.onkey(snake.go_south, "Down")
window.onkey(snake.go_west, "Left")
window.onkey(snake.go_east, "Right")
window.listen()

while True:
    window.update()
    time.sleep(0.1)
    snake.move()


window.exitonclick()
