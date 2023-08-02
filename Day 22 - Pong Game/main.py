from turtle import Screen
from pong import Paddle
from ball import Ball
from artist import Artist, Scoreboard
import time


# noinspection PyShadowingNames
def initialize_game():
    screen = Screen()
    screen.setup(1200, 598)
    screen.bgcolor("black")
    screen.title("The Best Pong")
    screen.tracer(0)

    player1 = Paddle(-1)
    player2 = Paddle(1)
    ball = Ball()
    ball.spawn()
    player1_score = Scoreboard(-1)
    player2_score = Scoreboard(1)

    net = Artist()
    net.draw_net()

    screen.listen()
    screen.onkey(player1.up, "w")
    screen.onkey(player1.down, "s")
    screen.onkey(player2.up, "Up")
    screen.onkey(player2.down, "Down")

    #   ---------------------------------------------------------------
    #    Ball Dev Tools. Move by i/k/j/l, press Q to show ball location.
    #    Enable in ball.py as well
    #
    # Artist.show_grids()
    #
    # screen.onkey(ball.up, "i")
    # screen.onkey(ball.down, "k")
    # screen.onkey(ball.go_left, "j")
    # screen.onkey(ball.go_right, "l")
    # screen.onkey(ball.ball_loc, "q")
    #   ---------------------------------------------------------------

    game_on = True

    return screen, player1, player2, player1_score, player2_score, ball, net, game_on


if __name__ == "__main__":
    screen, player1, player2, player1_score, player2_score, ball, net, game_on = initialize_game()

    while game_on:
        time.sleep(0.05)
        ball.ball_game(player1, player2, player1_score, player2_score)
        screen.update()
        if 5 in [player1_score.score, player2_score.score]:
            game_on = False

    net.game_over(player1_score.score, player2_score.score)
    ball.ht()
    screen.update()
    screen.exitonclick()
