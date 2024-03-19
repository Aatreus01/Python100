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

    def generate_car(self):
        random_y = randint(-250, 250)
        self.setpos(300, random_y)
        self.setheading(180)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.random_color()
    
    def random_color(self):
        x = randint(0, len(COLORS) - 1)
        self.color(COLORS[x])
        
    def move_car(self):
        self.forward(STARTING_MOVE_DISTANCE)