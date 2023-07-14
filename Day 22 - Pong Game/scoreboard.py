from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.score = 0
        self.write_score()



    def add_score(self):
        self.score += 1
        self.write_score()


    def write_score(self):
        self.clear()
        self.goto(-50, 260)
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)





    def game_over(self):
        self.clear()
        self.home()
        self.write(f"Game over, your score was {self.score}", align=ALIGNMENT, font=FONT)

    def draw_net(self):
        self.pensize(6)
        self.goto(0, -260)
        self.setheading(90)
        for _ in range(5):
            self.pendown()
            self.forward(40)
            self.penup()
            self.forward(80)
