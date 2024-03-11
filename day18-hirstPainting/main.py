import turtle as t
from random import choice

tim = t.Turtle()
t.colormode(255)
color_list = [(223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), 
            (218, 60, 84), (229, 79, 43), (195, 130, 169), (54, 168, 114), (28, 61, 116), (172, 53, 95), (108, 182, 90), (110, 99, 87), (193, 187, 46), (240, 204, 2), 
            (1, 102, 119), (19, 22, 21), (50, 150, 109), (172, 212, 172), (118, 36, 34), (221, 173, 188), (227, 174, 166), (153, 205, 220), (184, 185, 210)]
tim.pu()
tim.speed("fastest")
y = -200
x = -250
tim.setpos(x, y)

def draw_dot_line(num):
    for _ in range(num):
        color = choice(color_list)
        tim.dot(20, color)
        tim.forward(50)

repeat = 10

for _ in range(repeat):
    draw_dot_line(10)
    y += 50
    tim.setpos(x, y)

tim.hideturtle()



screen = t.Screen()
t.exitonclick()