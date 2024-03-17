from turtle import Screen, Turtle
import paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

pos_right = (350, 0)
pos_left = (-350, 0)
paddle_r = paddle.Paddle(pos_right)
paddle_l = paddle.Paddle(pos_left)

game_is_on = True
while game_is_on:
    screen.update()
    screen.listen()
    screen.onkey(key="w", fun=paddle_l.moveUp)
    screen.onkey(key="s", fun=paddle_l.moveDown)
    screen.onkey(key="Up", fun=paddle_r.moveUp)
    screen.onkey(key="Down", fun=paddle_r.moveDown)





screen.exitonclick()