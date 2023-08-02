from turtle import Screen
from player import Player
from car import Car
from interface import Artist
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("YOU SHALL NOT PASS!")
screen.bgcolor("grey")
screen.tracer(0)

screen.listen()

player = Player()
car = Car()
interface = Artist()

screen.onkeypress(player.move, "Up")

interface.draw_lines()

game_on = True

car_list = []

while game_on:
    screen.update()
    time.sleep(0.1)
    car_object = car.create_traffic()
    car_list.append(car_object)
    for car in car_list:
        car.move_traffic(car)
    # TODO: Needs some tinkering and fixing, the functions are a bit weird
    # TODO: Also. maybe use threading? How to pause a separate function?



screen.exitonclick()