from turtle import Turtle
from random import random, randint
import time


class Car(Turtle):
    car_starting_position = (310, 275 - (50 * randint(1, 8)))

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color((random(), random(), random()))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()

    def create_traffic(self):
        car = Car()
        car.goto(260, 275 - (50 * randint(1, 9)))
        car.setheading(180)
        return car

    def move_traffic(self, car):
        car.forward(10)
