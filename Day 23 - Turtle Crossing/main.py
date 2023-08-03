from turtle import Screen
from player import Player
from car import Car
from interface import Artist
import time
from threading import Timer



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


car_object = Car()
# traffic_timer = Timer(1, car_object.create_traffic)
# traffic_timer.start()
timer = 0
# car_object.create_traffic()

while game_on:
    time.sleep(0.1)
    timer += 1
    screen.update()
    if timer % 20 == 0:
        car_object.create_traffic()
    for car in car_object.car_list:
        car.move_car(car)
        game_on = player.check_collision(car)



# traffic_timer.cancel()

    # TODO: Needs some tinkering and fixing, the functions are a bit weird
    # TODO: Also. maybe use threading? How to pause a separate function?

screen.exitonclick()