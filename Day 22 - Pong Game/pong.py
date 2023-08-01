from turtle import Turtle

STARTING_Y = [40, 20, 0, -20, -40]  # Creates 3 block paddles. Just add a coordinate to make more block paddle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.paddle = []
        for position in STARTING_Y:
            # self.paddle.append(self.create_paddle(x, position))
            self.create_paddle(x, position)

    def create_paddle(self, x, y):
        paddle_block = Turtle()
        paddle_block.color("white")
        paddle_block.penup()
        paddle_block.shape("square")
        paddle_block.goto(x, y)
        self.paddle.append(paddle_block)

    def up(self):
        if self.paddle[0].ycor() < 280:
            for x in self.paddle:
                x.setheading(UP)
                x.forward(20)


    def down(self):
        if self.paddle[-1].ycor() > -280:
            for x in self.paddle:
                x.setheading(DOWN)
                x.forward(20)