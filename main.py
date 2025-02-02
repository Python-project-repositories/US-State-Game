
import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data["state"].tolist()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="Guess a state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_state:
            if state not in guessed_state:
                missing_states.append(state)
        print(f"You guessed {len(guessed_state)}/50 states correctly!")
        print(f"States to Learn: {', '.join(missing_states)}")
        break

    if answer_state in all_state:
        if answer_state not in guessed_state:
            guessed_state.append(answer_state)
            tur = turtle.Turtle()
            tur.hideturtle()
            tur.penup()
            state_data = data[data.state == answer_state]
            tur.goto(int(state_data.x), int(state_data.y))
            tur.write(state_data.state.item(), align="center", font=("Arial", 8, "normal"))


