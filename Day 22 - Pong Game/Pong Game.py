from turtle import Screen
# from pong import Pong
# from ball import Ball
from artist import Artist, Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("The Best Pong")
score_positions = [-50, 50]
players = []
screen.tracer(0)

for x in score_positions:
    player = Scoreboard(x)
    players.append(player)


net = Artist()
net.draw_net()
net.game_over(1,2)



screen.exitonclick()
