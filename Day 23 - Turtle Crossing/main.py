from turtle import Screen
from player import Player
from car import Car
from interface import Artist
import time


def initialization():
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
    speed = 0

    return car, interface, game_on, car_object, timer, speed, screen, player


if __name__ == "__main__":
    car, interface, game_on, car_object, timer, speed, screen, player = initialization()
    while game_on:
        time.sleep(0.05)
        timer += 1
        screen.update()
        if timer % 5 == 0:
            car_object.create_traffic()
        for car in car_object.car_list:
            car.move_car(car, speed)
            game_on = player.check_collision(car)
            if not game_on:
                interface.game_over()
                break
        if player.check_win():
            player.spawn()
            interface.add_level()
            speed += 3

    screen.exitonclick()
