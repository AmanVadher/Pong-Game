from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scorboard import Scorboard
import time

sc=Screen()
sc.setup(width=800,height=600)
sc.bgcolor("black")
sc.title("Pong")
sc.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball=Ball()
scoreboard = Scorboard()

sc.listen()
sc.onkey(r_paddle.go_up,"Up")
sc.onkey(r_paddle.go_down,"Down")
sc.onkey(l_paddle.go_up,"w")
sc.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    sc.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect r_paddle miss ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect l_paddle miss ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

sc.exitonclick()
