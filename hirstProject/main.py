# from colorgram import extract
# rgb_colors = []
# colors = extract('hirst.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
from random import choice
from hirstfunc import draw_circle
turtle.colormode(255)
colorlist = [(229, 218, 199), (145, 90, 49), (197, 159, 116), (200, 166, 18), (57, 103, 131), (25, 14, 10), (137, 72, 90), (20, 47, 75), (68, 114, 93), (215, 198, 148), (130, 20, 36), (69, 23, 35), (15, 52, 38), (18, 89, 60), (189, 137, 149), (145, 26, 13), (138, 168, 153), (123, 157, 170), (180, 97, 112), (193, 99, 80), (204, 218, 207), (92, 149, 119), (41, 59, 97), (7, 87, 106), (78, 104, 9), (83, 144, 157), (204, 219, 227), (225, 177, 166), (235, 212, 217), (229, 166, 174)]

bean = Turtle()
bean.shape("turtle")
bean.pensize(2)
bean.speed(0)
bean.hideturtle()
no_column = 10
no_row = 10
gap_amount = 80
circle_radius = 20
bean.penup()
y = -250

for _ in range(no_row):
    bean.goto(-350, y)
    for _ in range(no_column):
        draw_circle(bean, circle_radius, choice(colorlist))
        bean.forward(gap_amount)
    y += 50


screen = Screen()
turtle.exitonclick()