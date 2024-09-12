import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # get the coordinate on click
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

# 3: Use a loop to allow user to keep guessing
while len(guessed_states) < 50:
    # 4: Convert the guess to Title case
    # 5: Record the correct guesses in a list
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":  # exit the game
        # record the missing states using comprehensive dict
        missing_states = [state for state in all_states if state not in guessed_states]

        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        # print(missing_states)
        # turn the missing states list to csv
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break  # break out of the loop

    # 1: Check if the guess is among 50 states
    if answer_state in all_states:
        guessed_states.append(answer_state)  # add new state
        t = turtle.Turtle()  # create a turtle
        t.hideturtle()
        t.penup()

        # 2: Write correct guesses onto the map
        state_data = data[data.state == answer_state]  # get the row of data correspond to the state
        t.goto(int(state_data.x), int(state_data.y))  # take the coordinates
        # t.write(state_data.state.item())  # item(): return the first element of the underlying data
        t.write(answer_state)
