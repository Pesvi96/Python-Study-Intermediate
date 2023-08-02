from turtle import Turtle



class Artist(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.penup()
        self.pensize(2)

    def draw_lines(self):
        for x in range(10):
            self.goto(-300, -200 + (100*x))
            self.setheading(0)
            for _ in range(10):
                self.pendown()
                self.forward(20)
                self.penup()
                self.forward(40)

            self.goto(-300, -150 + (100*x))
            self.setheading(0)
            for _ in range(10):
                self.forward(40)
                self.pendown()
                self.forward(20)
                self.penup()
