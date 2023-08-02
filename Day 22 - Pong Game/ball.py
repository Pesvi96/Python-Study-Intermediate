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

    #       Could have just written self.goto(current_x, delta_x)
    #       and then delta_x will change the sign from time to time
    def move(self):
        self.setheading(self.x_heading)
        self.forward(20)
        self.setheading(self.y_heading)
        self.forward(20)

    #       Could have made this code much more readable by
    #       making separate functions for bounce events, but then you'd have
    #       to change the move function
    def ball_game(self, p1, p2, p1_score, p2_score):
        p1_cor = p1.ycor()
        p2_cor = p2.ycor()
        self.move()
        if self.ycor() >= 280:
            self.y_heading = DOWN
        elif self.ycor() <= -280:
            self.y_heading = UP
        if 530 <= self.xcor() <= 560 and p2_cor+50 >= self.ycor() >= (p2_cor - 50):
            # if ball is in the paddle vertical zone
            # and in proximity of first paddle turtle or -100s
            self.x_heading = LEFT
        elif -560 <= self.xcor() <= -530 and p1_cor+50 >= self.ycor() >= (p1_cor - 50):
            self.x_heading = RIGHT
        elif int(self.xcor()) <= -620:
            self.clear()
            self.spawn()
            p2_score.add_score()
        elif int(self.xcor()) >= 620:
            self.clear()
            self.spawn()
            p1_score.add_score()

    #   ---------------------------------------
    #   Ball Dev tools
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
