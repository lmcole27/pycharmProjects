from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(width=500, height=400)
race_on = False
answer = screen.textinput("Place a bet. ", "Which colour do you expect to win? Enter a colour: ")
colour_list = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

if answer:
    race_on = True

x = -220
y = -120

for turtle in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colour_list[turtle])
    new_turtle.penup()
    new_turtle.goto(x, y)
    all_turtles.append(new_turtle)
    y += 40

while race_on == True:
    for turtle in all_turtles:
        if turtle.xcor() >= 200:
            race_on = False
            if turtle.pencolor() == answer:
                print(f"You win!  You bet {answer} and the {turtle.pencolor()} turtle won the race.")
            else:
                print(f"You lose!  You bet {answer} and the {turtle.pencolor()} turtle won the race.")
        else:
            turtle.forward(randint(0, 10))
# race_turtles = []
# for turtle in range(6):
#     turtle_name = "turtle_" + colour_list[turtle]
#     # race_turtles
#     # turtle_name = t.Turtle()
#     # turtle_name = t.color(colour_list[turtle])
#     print(turtle_name)

screen.exitonclick()
