from turtle import Turtle
#import random
#STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, xcor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(xcor, 0)
        self.shapesize(stretch_wid=0.2, stretch_len=5)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def stop(self):
        self.forward(0)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.back(MOVE_DISTANCE)

