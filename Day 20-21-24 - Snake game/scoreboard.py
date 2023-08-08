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
        with open("score.txt", mode="r+") as file:
            self.high_score = int(file.read())
        self.write_score()


    def add_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        print(self.score)
        self.clear()
        self.write(f"Score: {self.score}, High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="r+") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.write_score()




    # def game_over(self):
    #     self.clear()
    #     self.home()
    #     self.write(f"Game over, your score was {self.score}", align=ALIGNMENT, font=FONT)
