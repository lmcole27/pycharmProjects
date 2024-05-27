from turtle import Turtle
FONT = ("courier", 18, "bold")


class ScoreBoard(Turtle):
    def __init__(self, level):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.update(level)

    def update(self, level):
        self.goto(-25, 360)
        self.clear()
        self.write(f"LEVEL {level}", True, align="left", font=FONT)

    def game_over(self):
        self.goto(-60, 0)
        self.write("GAME OVER", True, align="left", font=FONT)


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
