from turtle import Turtle
from random import choice
import time

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.x_heading = 0
        self.y_heading = 0

    def spawn(self):
        self.clear()
        self.home()
        self.x_heading = choice([LEFT, RIGHT])
        self.y_heading = choice([UP, DOWN])


    def move(self):
        self.setheading(self.x_heading)
        self.forward(20)
        self.setheading(self.y_heading)
        self.forward(20)

    def ball_game(self, p1, p2):
        self.move()
        if self.ycor() >= 280:
            self.y_heading = DOWN
        if self.ycor() <= -280:
            self.y_heading = UP
        print(f"ball {self.ycor()}")
        print(f"player {p1}")
        if 540 <= self.xcor() <= 560 and p2 >= self.ycor() >= (p2 - 100):
            # if ball is in the paddle vertical zone
            # and in proximity of first paddle turtle or -100s
            print("what")
            self.x_heading = LEFT
        if -560 <= self.xcor() <= -540 and p1 >= self.ycor() >= (p1 - 100):
            self.x_heading = RIGHT
            print("what")
        if int(self.xcor()) <= -600:
            self.clear()
            self.spawn()
            print("\n\n\t spawning\n\n")
            return "player1"
        if int(self.xcor()) >= 600:
            self.clear()
            self.spawn()
            print("\n\n\t spawning\n\n")
            return "player2"


