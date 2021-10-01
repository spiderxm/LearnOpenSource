
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time



# TODO 1. create the screen done
# TODO 2. create and move paddle
# TODO 3. create another paddle
# TODO 4. create ball and make it move
# TODO 4. detect collision and bounce back
# TODO 4. collison with paddle
# TODO 4. when paddle misses
# TODO 4. keep score


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()










screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



game_is_on = True
while game_is_on:
    time.sleep(move_speed)
    screen.update()
    ball.move()


    #? collision Logic
    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()

    #collision with r paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() >-320 :

        ball.bounce_x()

    if ball.xcor() >380:
        ball.reset_positions()
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reset_positions()
        scoreboard.r_point()


screen.exitonclick()
