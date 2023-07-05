from turtle import Turtle, Screen

screen = Screen()
bobby = Turtle()
bobby.fillcolor("DarkRed")
bobby.shape("turtle")
bobby.pensize(10)


# bobby.speed(5)


def w():
    bobby.forward(20)


def s():
    bobby.back(20)


def d():
    bobby.right(20)


def a():
    bobby.left(20)


def c():
    bobby.home()
    bobby.clear()


screen.listen()
screen.onkey(w, "w")
screen.onkey(a, "a")
screen.onkey(s, "s")
screen.onkey(d, "d")
screen.onkey(c, "c")

screen.exitonclick()
