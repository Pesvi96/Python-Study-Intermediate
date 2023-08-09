from turtle import Screen
from apostle import Apostle
import pandas


def initialize():
    screen = Screen()
    img = "./blank_states_img.gif"
    screen.setup(725, 491)
    screen.bgpic(img)
    apostle = Apostle()
    return screen, apostle


def get_data():
    my_dict = {}
    data = pandas.read_csv("50_states.csv")

    names = data["state"].tolist()
    for name in names:
        state = data[data["state"] == name]
        x_cor = state.x
        y_cor = state.y
        my_dict.update({name: [x_cor, y_cor]})
    print(my_dict)
    return my_dict


# TODO: შეცვალე ისე რომ State-ბში იპოვოს შტატი, და ამ შტატის row-დან მერე აიღოს data.x და data.y
