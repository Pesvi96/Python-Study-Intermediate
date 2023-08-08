from turtle import Turtle
from random import random, randint


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_list = []

    def create_traffic(self):
        car = Car()
        car.shape("square")
        car.color((random(), random(), random()))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.showturtle()
        car.goto(320, 275 - (50 * randint(1, 9)))   # Goes to right side, random lane
        car.setheading(180)
        # print("car created")
        self.car_list.append(car)

    @staticmethod
    def move_car(car, add):
        car.forward(5+add)
