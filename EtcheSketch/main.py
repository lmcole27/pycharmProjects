import turtle as t

eli = t.Turtle()
t.listen()

def move_forward():
    eli.forward(25)

def move_backward():
    eli.backward(25)

def turn_counterclock():
    eli.left(10)

def turn_clock():
    eli.right(10)


t.onkeypress(t.resetscreen, "c")
t.onkeypress(move_forward, "w")
t.onkeypress(move_backward, "s")
t.onkeypress(turn_counterclock, "a")
t.onkeypress(turn_clock, "d")

screen = t.Screen()
screen.exitonclick()