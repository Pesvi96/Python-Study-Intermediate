from turtle import Screen
from pong import Paddle
from ball import Ball
from artist import Artist, Scoreboard
import time

score_position = 50
paddle_position = 550
players = []  # list with 2 objects of Scoreboard class

screen = Screen()
screen.setup(1200, 598)
screen.bgcolor("black")
screen.title("The Best Pong")
screen.listen()
screen.tracer(0)
player1 = Paddle(paddle_position * -1)
player2 = Paddle(paddle_position)

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

ball = Ball()
ball.spawn()

while True:
    time.sleep(0.05)
    p1cor = player1.paddle[0].ycor()
    p2cor = player2.paddle[0].ycor()
    result = ball.ball_game(p1cor, p2cor)
    if result == "player1":
        players[0].add_score()
    elif result == "player2":
        players[1].add_score()
    print(players)
    screen.update()
    player_scores = [players[0].score, players[1].score]
    if 2 in player_scores:
        break

ball.hideturtle()
net.game_over(*player_scores)
screen.exitonclick()
