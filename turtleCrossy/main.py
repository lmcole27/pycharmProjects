from turtle import Screen
import time
from player import Player, ScoreBoard
from cars import Car_Manager

screen = Screen()
screen.setup(width=800, height=800)
screen.tracer(0)

game_on = True
level = 1
move_distance = 5

player = Player()
car_manager = Car_Manager()
score_board = ScoreBoard(level)

screen.update()
screen.listen()
screen.onkey(fun=player.move, key="Up")

while game_on:
    screen.update()
    time.sleep(.2)
    car_manager.create_car()
    car_manager.drive(move_distance)
    for car in car_manager.cars:
        if car.distance(player) < 25:
            game_on = False
            score_board.game_over()
            print("GAME OVER")
    if player.ycor() > 300:
        level += 1
        move_distance += 10
        score_board.update(level)
        player.new_level()
        print(f"Congratulations. You made it to level {level}!")



    if player.ycor() > 350:
        print("LEVEL 2")



screen.exitonclick()
