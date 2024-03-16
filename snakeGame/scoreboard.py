from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        score = 0
        self.pu()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {score}", align="center", font=("Comic Sans", 20, "normal"))