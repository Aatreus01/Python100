from turtle import Screen, Turtle
import paddle
import ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

pos_right = (350, 0)
pos_left = (-350, 0)
paddle_r = paddle.Paddle(pos_right)
paddle_l = paddle.Paddle(pos_left)
ball = ball.Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=paddle_l.moveUp)
screen.onkey(key="s", fun=paddle_l.moveDown)
screen.onkey(key="Up", fun=paddle_r.moveUp)
screen.onkey(key="Down", fun=paddle_r.moveDown)


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # detect right player miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # detect left player miss 
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()