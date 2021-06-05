import turtle

import tkinter
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = turtle.Screen()
screen.setup(width=580, height=580)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

img = tkinter.Image("photo", file="snake.png")
turtle._Screen._root.iconphoto(True, img)

snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.09)
    snake.move()
    score.clear()
    score.write_score()

    # Detect with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score += 1
        snake.extend()

    # Detect with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[2:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 8:
            score.reset()
            snake.reset()


screen.exitonclick()
