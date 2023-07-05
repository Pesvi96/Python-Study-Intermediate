from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Welcome to the Turtle Race, the fastest race on planet Earth!")
colors = ["blue", "red", "brown", "purple", "green", "violet", "orange", "magenta", ]
racers = []
racer_colors = []


def place_bets():
    amount = int(screen.numinput(title="Racer amount",
                                 prompt="Please state how many racers would you like to watch"))
    while amount < 2:
        amount = int(screen.numinput(title="Racer amount",
                                     prompt="Wrong input, please state your amount. It should be more than 1"))

    create_racers(amount)

    player_bet = screen.textinput(title="Bet",
                                  prompt=f"Welcome to the race. Place your bet please."
                                         f"You can bet on the following contestants: "
                                         f"{', '.join(racer_colors)}").lower()
    while player_bet not in racer_colors:
        player_bet = screen.textinput(title="Bet", prompt=f"Wrong choice, please choose from: "
                                                          f"{', '.join(racer_colors)}").lower()
    return amount, player_bet


def create_racers(amount):
    for x in range(amount):
        racer = Turtle(shape="turtle")
        racer_color = choice(colors)
        colors.remove(racer_color)
        racer.color(racer_color)
        racer_colors.append(racer_color)
        racer.penup()
        racer.goto(-200, -150 + ((x + 1) * 300 / (amount + 1)))
        racers.append(racer)
    return racers


def race():
    race_on = True
    while race_on:
        for turtle in racers:
            turtle.forward(randint(5, 20))
            if turtle.xcor() >= 200:
                if turtle.pencolor() == player_bet:
                    screen.textinput(title="You win", prompt="Congratulations, you win!")
                else:
                    screen.textinput(title="You lose", prompt=f"Next time maybe. "
                                                              f"The winner was {turtle.pencolor()}")
                race_on = False
                break


amount, player_bet = place_bets()
race()
screen.bye()
