from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.goto(position)
        
    def moveUp(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def moveDown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)