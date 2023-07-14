from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("The Best Snake Game")
screen.tracer(0)

game_on = True

# main
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # Detect collision with food
    if snake.check_distance(food):
        food.new_food()
        scoreboard.add_score()
        snake.extend()

    # Detect collision with tail
    for tail_part in snake.snake[1:]:
        if snake.check_distance(tail_part):
            scoreboard.game_over()
            game_on = False

    # Detect collision with wall
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        scoreboard.game_over()
        game_on = False

screen.exitonclick()
