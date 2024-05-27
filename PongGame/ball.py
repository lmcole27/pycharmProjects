from turtle import Turtle

MOVE_DISTANCE = 20

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        #self.setheading(45)
        self.x_move = 10
        self.y_move = 10
        #self.shapesize(stretch_wid=0.2, stretch_len=5)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
