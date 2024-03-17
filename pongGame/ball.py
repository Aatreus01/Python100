from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
    
    def move(self):
        self.goto(self.xcor() + 0.1, self.ycor() + 0.1)