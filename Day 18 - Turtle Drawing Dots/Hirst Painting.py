import colorgram
from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.colormode(255)
bobby = Turtle()
bobby.color("DarkRed")
bobby.shape("arrow")
bobby.pensize(10)
bobby.penup()
bobby.speed(0)
rgb = []
bobby.setpos(-250, -250)
bobby.hideturtle()

color_palette = colorgram.extract("Dall-E.png", 30)
print(f"size will be {len(color_palette)}")

for color in color_palette:
    rgb.append((color.rgb[0], color.rgb[1], color.rgb[2]))

for k in range(10):
    for x in range(10):
        bobby.dot(20, choice(rgb))
        bobby.forward(50)
    current_y = bobby.ycor()
    bobby.setpos(-250, current_y+50)



screen.exitonclick()