from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.pu()
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.goto(-290, 270)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
