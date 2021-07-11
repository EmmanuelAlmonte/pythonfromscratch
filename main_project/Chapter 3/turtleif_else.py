import turtle




if turtle.xcor() > 249 or  turtle.ycor() > 349:
    turtle.goto()

if turtle.heading() >= 90 and turtle.heading () <= 270:
    turtle.setheading(180)

if turtle.isdown():
    turtle.penup()

if not(turtle.isdown):
    turtle.pendown()

if turtle.isvisible():
    turtle.hideturtle()

if turtle.pencolor() == 'red':
    turtle.pencolor('blue')

if turtle.fillcolor() == 'blue':
    turtle.fillcolor('white')

if turtle.bgcolor() == 'white':
    turtle.fillcolor('gray')

if turtle.speed() > 0:
    turtle.speed(0)






