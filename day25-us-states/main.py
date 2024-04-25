import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("Amariga Oyun")
image = "..\\day25-us-states\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.pu()
writer.hideturtle()

data = pd.read_csv("..\\day25-us-states\\50_states.csv")
all_states = data.state.to_list()

answer_state = screen.textinput(title="Guess the State", prompt="What's another State's name?")
print(answer_state)

if answer_state in all_states:
    state_data = data[data.state == answer_state]
    writer.goto(int(state_data.x), int(state_data.y))
    writer.write(data.state, align="center")



turtle.mainloop()
