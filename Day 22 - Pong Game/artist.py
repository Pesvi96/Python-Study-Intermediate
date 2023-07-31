from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Artist(Turtle):

    def __init__(self):     # Invisible white chuvak
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()

    def draw_net(self):
        self.pensize(6)
        self.goto(0, -260)
        self.setheading(90)
        for _ in range(5):
            self.pendown()
            self.forward(40)
            self.penup()
            self.forward(80)

    def game_over(self, player_one, player_two):
        self.clear()
        self.home()
        self.write(f"Game over, the score was {player_one} : {player_two}",
                   align=ALIGNMENT, font=("Courier", 25, "normal"))


class Scoreboard(Artist):

    def __init__(self, x):
        super().__init__()
        self.goto(x, 240)
        self.score = 0
        self.write_score()

    def add_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

