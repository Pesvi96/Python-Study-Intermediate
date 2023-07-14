from turtle import Screen
# from pong import Pong
# from ball import Ball
from scoreboard import Scoreboard
import time



screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("The Best Pong")
# screen.tracer(0)

player_one = Scoreboard()
net = Scoreboard()
net.draw_net()

player_one.add_score()


screen.exitonclick()