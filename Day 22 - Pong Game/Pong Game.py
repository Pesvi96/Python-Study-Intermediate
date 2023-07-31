from turtle import Screen
# from pong import Pong
# from ball import Ball
from artist import Artist, Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("The Best Pong")
# score_positions = [-50, 50]
score_position = 50
pong_position = 350
players = []        # list with 2 objects of Scoreboard class
screen.tracer(0)

for _ in range(2):
    score_position = score_position * -1
    player = Scoreboard(score_position)
    players.append(player)


net = Artist()
net.draw_net()
net.game_over(1,2)



screen.exitonclick()
