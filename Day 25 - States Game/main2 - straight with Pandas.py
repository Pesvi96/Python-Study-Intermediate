import pandas as pd
from functions import *

if __name__ == "__main__":
    screen, apostle = initialize()
    data = pd.read_csv("50_states.csv")

    guessed = []
    while len(guessed) < 50:
        guess = screen.textinput(f"{len(guessed)}/50 States Guessed", "Please input the State name").title()
        if guess == "Exit":
            break
        if guess in data.state.values and guess not in guessed:
            print("it's here")
            x_cor = data[data.state == guess].x.item()
            y_cor = data[data.state == guess].y.item()
            print(x_cor)
            print(y_cor)
            apostle.write_state(guess, [x_cor, y_cor])

            guessed.append(guess)



    remained_states = [n for n in data.state.tolist() if n not in guessed]
    # Much easier, list comprehension way 👆
    # remained_states = data.state.tolist()
    # for state in guessed:
    #     remained_states.remove(state)
    # print(remained_states)
    csv = pd.DataFrame(remained_states)
    csv.to_csv("Guessed_list.csv")
    screen.exitonclick()
