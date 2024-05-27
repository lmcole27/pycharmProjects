import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()


def set_screen():
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    screen.listen()


set_screen()
game_on = True
snake = Snake()
food = Food()
scoreboard = ScoreBoard()


def set_screen_actions():
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(game_reset, "p")


def game_reset():
    screen.clear()
    set_screen()
    set_screen_actions()
    scoreboard.reset()
    time.sleep(1)
    snake.reset()
    food.new_food()

set_screen_actions()

while game_on:
    screen.update()
    scoreboard.display()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 25:
        food.refresh()
        scoreboard.score += 1
        scoreboard.display()
        snake.extend()
        snake.extend()
        snake.extend()
        snake.extend()
        snake.extend()

    if snake.head.xcor() > 450 or snake.head.xcor() < -450 or snake.head.ycor() > 400 or snake.head.ycor() < -400:
        time.sleep(1)
        game_reset()

    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 20:
            game_on = False



screen.exitonclick()
