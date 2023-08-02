from turtle import Turtle

MOVE_DISTANCE = 20
paddle_position = 550


class Paddle(Turtle):
    def __init__(self, x):
        global paddle_position
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(paddle_position * x, 0)

    def up(self):
        if self.ycor() < 280:
            self.goto(self.xcor(), self.ycor()+MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -280:
            self.goto(self.xcor(), self.ycor()-MOVE_DISTANCE)
