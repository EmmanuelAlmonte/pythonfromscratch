import turtle, random
turtle.hideturtle()
turtle.speed(0)

def create_square(size):
    for s in range(4):
        turtle.forward(size)
        turtle.right(90)

def create_circle(radius):
    turtle.circle(radius)


