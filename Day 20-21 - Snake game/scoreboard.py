from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def add_score(self):
        self.score += 1
        print(self.score)
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.clear()
        self.home()
        self.write(f"Game over, your score was {self.score}", align=ALIGNMENT, font=FONT)

