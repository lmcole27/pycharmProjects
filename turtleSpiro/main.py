import turtle
from turtle import Turtle, Screen
from random import choice, randint
turtle.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color

olive = Turtle()
olive.shape("turtle")
olive.pensize(2)
olive.speed(0)
gap_amount = 5


for _ in range(int(360/gap_amount)):
    olive.pencolor(random_color())
    olive.circle(100)
    olive.setheading(olive.heading() + gap_amount)

screen = Screen()
turtle.exitonclick()