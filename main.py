import turtle as t
import pandas
screen = t.Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
t.shape(image)
states_50 = []
remaining_states = []
n = 0
data = pandas.read_csv('50_states.csv')
list_of_states = data['state'].tolist()
while len(states_50) < 50:
    answer = screen.textinput(title=f'Guess the state {n}/50', prompt='What\'s another state').title()
    states_50.append(answer)
    if answer == "Exit":
        remaining_states = [state for state in list_of_states if state not in states_50]
        remaining_states = pandas.DataFrame(remaining_states)
        remaining_states.to_csv('remaining_states.csv')
        break
    for state in list_of_states:
        if answer == state:
            us_state = data[data.state == answer]
            new_state = t.Turtle()
            new_state.hideturtle()
            new_state.penup()
            new_state.goto(int(us_state.x), int(us_state.y))
            new_state.write(answer)
            n += 1

