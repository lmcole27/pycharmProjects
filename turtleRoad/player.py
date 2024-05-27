from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(0, -380)

    def move(self):
        self.forward(20)

    def new_level(self):
        self.goto(0, -380)
