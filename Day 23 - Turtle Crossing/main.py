from turtle import Screen
import time

screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)