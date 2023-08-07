from turtle import Turtle
from random import random, randint


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color((random(), random(), random()))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.hideturtle()
        self.car_list = []

    def create_traffic(self):
        car = Car()
        car.showturtle()
        car.goto(320, 275 - (50 * randint(1, 9)))
        car.setheading(180)
        # print("car created")
        self.car_list.append(car)

    @staticmethod
    def move_car(car):
        car.forward(10)
