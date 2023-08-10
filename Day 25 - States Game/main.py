# data = pandas.read_csv("226 weather-data.csv")
# max_temp = data.temp.max()
# print(max_temp)
# hottest_day = data[data.temp == max_temp]
# print(hottest_day)
# print()
# monday = data[data.day == "Monday"]
# mon_temp = (monday.temp*2)+30
# print(mon_temp)

# data_dict = {"students": ["Amy", "Robert", "Helen"],
#              "age": [13, 15, 18]}
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")


# data = pandas.read_csv("228 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
# colors_list = data["Primary Fur Color"].dropna()    # Brings out Primary Fur Color unique items as a list
# colors = colors_list.unique().tolist()
# black_count = len(data[data["Primary Fur Color"] == "Black"])
# gray_count = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
#
# counts = [gray_count, cinnamon_count, black_count]
# print(colors)
# print(counts)
# data_dict = {"Colors": colors, "Count": counts}
# print(data_dict)
#
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("new_data.csv")
# print(new_data)


from functions import *



if __name__ == "__main__":
    screen, apostle = initialize()
    my_dict = get_data()
    data = pd.read_csv("50_states.csv")
    guessed = []

    while len(guessed) < 50:
        guess = screen.textinput(f"{len(guessed)}/50 States Guessed", "Please input the State name").title()
        if guess == "Exit":
            break
        if guess in my_dict.keys() and guess not in guessed:
            print("Guessed correctly")
            apostle.write_state(guess, my_dict[guess])
            guessed.append(guess)


    remained_states = data.state.tolist()
    for state in guessed:
        remained_states.remove(state)
    print(remained_states)
    csv = pd.DataFrame(remained_states)
    csv.to_csv("Guessed_list.csv")
    screen.exitonclick()

    screen.exitonclick()


