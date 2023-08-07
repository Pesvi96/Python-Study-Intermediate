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

game_on = True

car_object = Car()
timer = 0
speed = 0.1

while game_on:
    time.sleep(speed)
    timer += 1
    screen.update()
    if timer % 5 == 0:
        car_object.create_traffic()
    for car in car_object.car_list:
        car.move_car(car)
        game_on = player.check_collision(car)
        if not game_on:
            interface.game_over()
            break
    if player.check_win():
        player.spawn()
        interface.add_level()
        speed *= 0.7

screen.exitonclick()
