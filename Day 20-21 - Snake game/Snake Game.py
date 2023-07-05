from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Best Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
snake = []
game_on = True

screen.tracer(0)



for position in starting_positions:
    tail_part = Turtle("square")
    tail_part.color("white")
    tail_part.penup()
    tail_part.speed(1)
    tail_part.goto(position)
    snake.append(tail_part)


while game_on:
    time.sleep(0.08)
    screen.update()
    for tail in range(start= 2, stop= 0, step= -1):
        pass





screen.exitonclick()