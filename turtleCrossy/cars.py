from turtle import Turtle, colormode
import random

colormode(255)
color_list = [(229, 218, 199), (145, 90, 49), (197, 159, 116), (200, 166, 18), (57, 103, 131), (25, 14, 10),
              (137, 72, 90), (20, 47, 75), (68, 114, 93), (215, 198, 148), (130, 20, 36), (69, 23, 35), (15, 52, 38),
              (18, 89, 60), (189, 137, 149), (145, 26, 13), (138, 168, 153), (123, 157, 170), (180, 97, 112),
              (193, 99, 80), (204, 218, 207), (92, 149, 119), (41, 59, 97), (7, 87, 106), (78, 104, 9), (83, 144, 157),
              (204, 219, 227), (225, 177, 166), (235, 212, 217), (229, 166, 174)]


class Car_Manager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()

    def create_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle()
            car.penup()
            car.color(random.choice(color_list))
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(380, random.randint(-340, 340))
            car.setheading(180)
            self.cars.append(car)

    def drive(self, move_distance):
        for car in self.cars:
            car.forward(move_distance)
