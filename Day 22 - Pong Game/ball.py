from turtle import Turtle
from random import choice

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
        self.goto(0, 0)
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
        if self.xcor() >= 320 and self.xcor() <= 350 and self.ycor() <= p1 and self.ycor() >= p1 - 100:
            # if ball is in the paddle vertical zone
            # and in proximity of first paddle turtle or -100s
            print("what")
            self.x_heading = RIGHT
        if self.xcor() <= -320 and self.xcor() >= -350 and self.ycor() <= p2 and self.ycor() >= p2 - 100:
            self.x_heading = LEFT
            print("what")
        if int(self.xcor()) <= -390 and int(self.xcor()) >= 390:
            self.spawn()
            print("\n\n\t spawning\n\n")


