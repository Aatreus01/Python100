import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = []


screen.listen()
screen.onkey(key="w", fun=player.move)

count = 5

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if count == 5:
        cars.append(CarManager())
        count = 0
    
    for car in cars:
        car.move_car()
    count += 1
