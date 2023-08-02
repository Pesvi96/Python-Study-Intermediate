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
        p1_cor = p1.ycor()
        p2_cor = p2.ycor()
        self.move()
        if self.ycor() >= 280:
            self.y_heading = DOWN
        if self.ycor() <= -280:
            self.y_heading = UP
        print(f"ball {self.ycor()}")
        print(f"player {p1}")
        if 530 <= self.xcor() <= 560 and p2_cor >= self.ycor() >= (p2_cor - 100):
            # if ball is in the paddle vertical zone
            # and in proximity of first paddle turtle or -100s
            print("what")
            self.x_heading = LEFT
        elif -560 <= self.xcor() <= -530 and p1_cor >= self.ycor() >= (p1_cor - 100):
            self.x_heading = RIGHT
            print("what")
        elif int(self.xcor()) <= -620:
            self.clear()
            self.spawn()
            print("\n\n\t spawning\n\n")
            p1.add_score()
        elif int(self.xcor()) >= 620:
            self.clear()
            self.spawn()
            print("\n\n\t spawning\n\n")
            p2.add_score()


        # Ball Dev tools
    #
    # def up(self):
    #     self.setheading(UP)
    #     self.forward(20)
    #
    # def down(self):
    #     self.setheading(DOWN)
    #     self.forward(20)
    #
    # def go_left(self):
    #     self.setheading(LEFT)
    #     self.forward(20)
    #
    # def go_right(self):
    #     self.setheading(RIGHT)
    #     self.forward(20)
    #
    # def ball_loc(self):
    #     print(self.position())

