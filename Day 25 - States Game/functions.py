from turtle import Screen
from apostle import Apostle
import pandas as pd


def initialize():
    screen = Screen()
    img = "./blank_states_img.gif"
    screen.setup(725, 491)
    screen.bgpic(img)
    apostle = Apostle()
    return screen, apostle


def get_data():
    my_dict = {}
    data = pd.read_csv("50_states.csv")

    for name in data.state:
        print(name)
        x_cor = data[data.state == name].x.iloc[0]
        y_cor = data[data.state == name].y.iloc[0]
        my_dict.update({name.capitalize(): [x_cor, y_cor]})

    print(my_dict)
    return my_dict

