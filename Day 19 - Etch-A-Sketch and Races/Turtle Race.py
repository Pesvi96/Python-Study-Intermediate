from turtle import Turtle, Screen
from random import choice

screen = Screen()
racers = []
colors = ["Blue", "Red", "Black", "Purple", "Green"]



for x in range(5):
    racers.append(Turtle())
    color = choice(colors)
    racers[x].color(color)
    racers[x].shape("turtle")
    racers[x].penup()
    racers[x].goto(-200, -100+(x*50))
    colors.remove(color)




print(racers)

# bobby = Turtle()
# bobby.fillcolor("DarkRed")
# bobby.shape("turtle")
# bobby.pensize(10)

screen.exitonclick()
