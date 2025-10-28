import time
from turtle import Screen

from ball import Ball
from center_line import CenterLine
from paddle import Paddle
from scoreboard import Scoreboard

window = Screen()
window.setup(width=800, height=600)
window.bgcolor("black")
window.tracer(0)

p1 = Paddle("left")
p2 = Paddle("right")
scoreboard = Scoreboard()
center_line = CenterLine()
ball = Ball()

window.onkeypress(p1.move_up, "a")
window.onkeypress(p1.move_down, "z")
window.onkeypress(p2.move_up, "Up")
window.onkeypress(p2.move_down, "Down")

window.listen()

while scoreboard.p1_score < 10 and scoreboard.p2_score < 10:
    window.update()
    time.sleep(0.002)
    ball.move()
    if ball.has_hit_wall():
        ball.bounce()
    for part in p1.parts:
        if ball.distance(part) < 20:
            ball.hit_paddle()
    for part in p2.parts:
        if ball.distance(part) < 20:
            ball.hit_paddle()
    if ball.is_out_of_field():
        if ball.xcor() < 0:
            scoreboard.p2_score += 1
        else:
            scoreboard.p1_score += 1
        scoreboard.update_score()
        ball.reset()
        ball.create()

window.exitonclick()
