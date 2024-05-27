from turtle import Turtle, Screen
FONT = ("courier", 18, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()

    def display(self):
        self.goto(-200, 350)
        self.clear()
        self.write(f"Score: {self.score}         High Score: {self.high_score}", True, align="left", font=FONT)

    def reset(self):
        print("scoreboard.reset")
        self.goto(-60, 15)
        self.write(f"GAME OVER", True, align="left", font=FONT)
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
            self.goto(-250, -20)
            self.write(f"CONGRATULATIONS YOU ACHIEVED A NEW HIGH SCORE: {self.score}", True, align="left", font=FONT)
        self.score = 0

    # def game_over(self):
    #     self.goto(-60, 0)
    #     self.write("GAME OVER", True, align="left", font=FONT)
