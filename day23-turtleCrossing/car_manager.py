from turtle import Turtle
from random import randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.pu()
        self.generate_car()
        self.speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_y = randint(-250, 250)
        self.setpos(310, random_y)
        self.setheading(180)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.random_color()
    
    def random_color(self):
        x = randint(0, len(COLORS) - 1)
        self.color(COLORS[x])
        
    def reset_pos(self):
        self.setpos(310, self.random_y)
        
    def set_speed(self, level):
        self.speed = (level*MOVE_INCREMENT) + STARTING_MOVE_DISTANCE   
        
    def move_car(self):
        random_y = randint(-250, 250)
        if self.xcor() < -320:
            self.goto(310, random_y)
        
        self.forward(self.speed)