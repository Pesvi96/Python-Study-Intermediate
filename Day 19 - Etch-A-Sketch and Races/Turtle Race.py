from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Welcome to the Turtle Race, the fastest race on planet Earth!")
colors = ["blue", "red", "brown", "purple", "green", "violet", "orange"]
player_bet = screen.textinput(title="Bet",
                              prompt="Welcome to the race. Place your bet please."
                                     "You can bet on the following contestants: "
                                     "Blue, Red, Brown, Purple, Green, Violet, Orange").lower()
while player_bet not in colors:
    player_bet = screen.textinput(title="Bet", prompt="Wrong choice, please choose from: "
                                  "Blue, Red, Brown, Purple, Green, Violet, Orange")


def create_racers():
    racers = {"Blue": None, "Red": None, "Brown": None, "Purple": None, "Green": None,
              "Violet": None, "Orange": None}
    count = 0
    for x in racers:
        racers[x] = Turtle(shape="turtle")
        racers[x].color(x)
        racers[x].penup()
        racers[x].goto(-200, -150 + (count * 50))
        count += 1
    print(racers)
    return racers


def race():
    race_on = True
    while race_on:
        for x in racers:
            turtle = racers[x]
            turtle.forward(randint(10, 50))
            if turtle.xcor() >= 180:
                if x == player_bet:
                    print("Congratulations, you win!")
                else:
                    print(f"Next time maybe. The winner was {x}")
                race_on = False
                break


racers = create_racers()
race()
screen.bye()
