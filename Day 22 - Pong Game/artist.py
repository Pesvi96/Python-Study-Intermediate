from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Artist(Turtle):

    def __init__(self):  # Invisible white chuvak
        super().__init__()
        self.color("white")
        self.shape("square")
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

    @staticmethod
    def show_grids():
        grid = Turtle()
        grid.penup()
        grid.goto(-600, -300)
        grid.color("red")
        grid.ht()
        grid.pendown()

        # x coordinates
        for _ in range(15):
            grid.setheading(90)
            grid.forward(600)
            grid.setheading(0)
            grid.forward(20)
            grid.setheading(270)
            grid.forward(600)
            grid.setheading(0)
            grid.forward(20)

        for _ in range(15):
            grid.setheading(180)
            grid.forward(600)
            grid.setheading(90)
            grid.forward(20)
            grid.setheading(0)
            grid.forward(600)
            grid.setheading(90)
            grid.forward(20)

    def game_over(self, player_one, player_two):
        self.clear()
        self.home()
        self.write(f"Game over, the score was {player_one} : {player_two}",
                   align=ALIGNMENT, font=("Courier", 25, "normal"))
        self.hideturtle()


#       You could have made one instance of Scoreboard,
#       which would have two attributes: player1_score and player2_score.
#       Then methods would change those attributes
class Scoreboard(Artist):
    score_position = 50

    def __init__(self, x):
        super().__init__()
        self.goto(Scoreboard.score_position * x, 240)
        self.ht()
        self.score = 0
        self.write_score()

    def add_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)
