from turtle import Turtle


class Artist(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.level = 1
        self.pensize(2)
        self.draw_lines()
        self.write_level()

    def draw_lines(self):
        for x in range(10):
            self.goto(-300, -200 + (100 * x))
            self.setheading(0)
            for _ in range(10):
                self.pendown()
                self.forward(20)
                self.penup()
                self.forward(40)

            self.goto(-300, -150 + (100 * x))
            self.setheading(0)
            for _ in range(10):
                self.forward(40)
                self.pendown()
                self.forward(20)
                self.penup()

    def game_over(self):
        self.color("black")
        self.home()
        self.write(f"Game Over", align="center", font=("Courier", 30, "bold"))

    def write_level(self):
        self.goto(-230, 270)
        self.color("black")
        self.write(f"Level: {self.level}", align="center", font=("Courier", 25, "bold"))

    def add_level(self):
        self.undo()
        self.level += 1
        self.write_level()
