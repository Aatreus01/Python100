from turtle import Turtle, Screen
from random import choice, randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color: ")
colors = ["blue", "red", "purple", "green", "orange", "pink"]
turtles = []

if user_bet:
    is_race_on = True

def create_turtle():
    color_choice = choice(colors)
    tim = Turtle(shape="turtle")
    tim.color(color_choice)
    tim.pu()
    colors.remove(color_choice)
    turtles.append(tim)

y = 100
x = -230
for i in range(6):
    create_turtle()
    turtles[i].goto(x, y)
    y -= 40

while is_race_on:
    for turtle in turtles:
        random_distance = randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()
            is_race_on = False
            if winner_color == user_bet:
                print(f"Tebrikler lan tahminin {winner_color} kazandı")
            else:
                print(f"Zaaa mal {winner_color} kazandı, sen {user_bet} seçmiştin")
screen.exitonclick()