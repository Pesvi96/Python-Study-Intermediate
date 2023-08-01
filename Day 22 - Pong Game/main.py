from turtle import Screen, Turtle
from pong import Paddle
from ball import Ball
from artist import Artist, Scoreboard
import time


score_position = 50
paddle_position = 350
pong_position = 350
players = []        # list with 2 objects of Scoreboard class



screen = Screen()
screen.setup(800, 598)
screen.bgcolor("black")
screen.title("The Best Pong")
screen.listen()
screen.tracer(0)
player1 = Paddle(paddle_position * -1)
player2 = Paddle(paddle_position)
def now():
    print("\n\n\t\t\t\t !!! NOW !!")
screen.onkey(now, "b")
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")




for _ in range(2):
    score_position = score_position * -1
    player = Scoreboard(score_position)
    players.append(player)


print(players)
net = Artist()
net.draw_net()

test = Turtle("square")
test.color("red")
test.penup()
test.goto(330, 100)

ball = Ball()
ball.spawn()



while True:
    time.sleep(0.2)
    p1cor = player1.paddle[0].ycor()

    p2cor = player2.paddle[0].ycor()
    ball.ball_game(p1cor, p2cor)
    screen.update()



screen.exitonclick()

# net.game_over(1,2)




