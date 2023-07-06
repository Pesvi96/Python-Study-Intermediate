from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
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

    # Detect collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        scoreboard.game_over()
        game_on = False

    # Detect collision with tail. ეგრევე გეიმ ოვერს ჩითავს, რ
    # ამენაირად უნდა შევცვალო რო დალაგების მერე გაჩითოს,
    # და ახალი ნაწილების დამატებისასაც არ ჩათვალოს რო დაეჯახა
    for tail_part in snake.snake:
        if snake.head.pos() == tail_part.pos():
            scoreboard.game_over()
            game_on = False


screen.exitonclick()
