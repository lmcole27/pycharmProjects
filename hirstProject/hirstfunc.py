def draw_circle(turtle, circle_radius, color):
    turtle.pendown()
    turtle.color(color, color)
    turtle.begin_fill()
    turtle.circle(circle_radius)
    turtle.end_fill()
    turtle.penup()
