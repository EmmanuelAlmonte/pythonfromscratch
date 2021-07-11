import turtle

# hide turtle
turtle.hideturtle()

LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

#Set the graphics window size to 500 pixels wide by 600 pixels high.
turtle.setup(500, 600)

turtle.penup()
turtle.goto(LEFT_SHOULDER_X,  # Left shoulder 
             LEFT_SHOULDER_Y) 
turtle.write("Betelguse")
turtle.dot()

turtle.goto(RIGHT_SHOULDER_X, # Right shoulder
              RIGHT_SHOULDER_Y) 
turtle.write("Meissa")
turtle.dot()

turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y) # Leftmost star in the belt 
turtle.write("Alntak")
turtle.dot()

turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y) #Middle star in the belt
turtle.write("Alnilam")
turtle.dot()

turtle.goto(RIGHT_BELTSTAR_X, 
               RIGHT_BELTSTAR_Y)  # Rightmost staturtle.goto
turtle.write("Mintaka")
turtle.dot()

turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y) # Left Knee
turtle.write("Saiph")
turtle.dot()

turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y) # Right Knee
turtle.write("Rigel") 
turtle.dot()

#Connect the dots.
# Left shoulder to left belt star
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)

# Right shoulder to right star 
turtle.penup()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)

# Left belt star to middle belt star
turtle.penup()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)

# Middle belt star to right belt star
turtle.penup()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)

# Left belt star to left knee
turtle.penup()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)

# Right belt to right knee 
turtle.penup()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
print(turtle.pos())

#To continuously show turtel screen.
turtle.mainloop()