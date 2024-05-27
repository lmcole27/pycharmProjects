import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
# from scoreboard import Scoreboard

screen = Screen()
screen.screensize(canvheight=600, canvwidth=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
s_turtle = Turtle("turtle")
s_turtle.hideturtle()
s_turtle.penup()
s_turtle.goto(0, 400)
s_turtle.pensize(2)
s_turtle.color("white")

s_turtle.setheading(270)
for i in range(20):
    s_turtle.pendown()
    s_turtle.forward(30)
    s_turtle.penup()
    s_turtle.forward(15)

r_paddle = Paddle(400)
l_paddle = Paddle(-400)
ball = Ball()
screen.update()

#screen.tracer(0)
# scoreboard = Scoreboard()
# scoreboard.display()
game_on = True

while game_on:
    screen.update()
    screen.listen()
    time.sleep(.15)
    ball.move()
    screen.onkey(r_paddle.up, "Up")
    screen.onkey(r_paddle.down, "Down")
    screen.onkey(l_paddle.up, "w")
    screen.onkey(l_paddle.down, "s")
    if ball.ycor() > 360 or ball.ycor() < -360:
        ball.bounce_y()
    if ball.xcor() > 360 or ball.xcor() < -360:
        if ball.distance(l_paddle) < 50 or ball.distance(r_paddle) < 50:
            ball.bounce_x()
        else:
            ball.goto(0, 0)
            ball.bounce_x()
            print("THE END")
    #screen.onkeyrelease(my_paddle.stop, "Up")
    #screen.onkeyrelease(my_paddle.stop, "Down")
    screen.update()


#
#     if snake.head.distance(food) < 25:
#         food.refresh()
#         scoreboard.score += 1
#         scoreboard.display()
#         snake.extend()
#         snake.extend()
#         snake.extend()
#         snake.extend()
#         snake.extend()
#
#     if snake.head.xcor() > 450 or snake.head.xcor() < -450 or snake.head.ycor() > 400 or snake.head.ycor() < -400:
#         game_on = False
#         scoreboard.game_over()
#
#
#
#     for segment in snake.segments[2:]:
#         if snake.head.distance(segment) < 25:
#             game_on = False
#             scoreboard.game_over()

screen.exitonclick()
