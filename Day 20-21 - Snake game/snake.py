from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            tail_part = Turtle("square")
            tail_part.color("white")
            tail_part.penup()
            tail_part.speed(1)
            tail_part.goto(position)
            self.snake.append(tail_part)

    def move(self):
        for tail_part in range(len(self.snake) - 1, 0, -1):
            next_loc = self.snake[tail_part - 1].pos()
            self.snake[tail_part].goto(next_loc)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def check_distance(self, object):
        if self.head.distance(object) < 10:
            return True
