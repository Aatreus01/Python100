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
level = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.detect_win():
        level += 1
    if count == 5 and len(cars) < 40:
        cars.append(CarManager())   # Spawn a car every 6th step of the loop
        count = 0
    for car in cars:
        if car.distance(player) < 20:
            game_is_on = False
            break
        car.set_speed(level) # Move the cars and detect collision
        car.move_car()
    
    count += 1


screen.exitonclick()