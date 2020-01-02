import turtle

# set up the windown
screen = turtle.Screen()
# ensure the size of the window will always be 300x500 ...
screen.setup(300, 500)

# background

# set the background color be black
screen.bgcolor("red")

# make the turtle faster
turtle.speed(10)
# set turtle pensize
turtle.pensize(3)
# set turtle pencolor be black
turtle.pencolor("black")

# draw mickey

# draw face

# move turtle
turtle.penup()
# turtle.goto(0,-60)
turtle.goto(-105, 130)
turtle.pendown()

# draw circle
turtle.fillcolor('black')
turtle.begin_fill()
turtle.circle(65)
turtle.end_fill()

# draw left ear

# move turtle
turtle.penup()
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.pendown()

# draw circle

turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# draw right ear

# move turtle
turtle.penup()
turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.forward(55)
turtle.right(90)
# draw circle

turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

turtle.left(90)


### red

turtle.pencolor("red")

# draw face

# move turtle
turtle.penup()
# turtle.goto(0,-55)
turtle.goto(-105, 135)
turtle.pendown()

# draw circle
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(60)
turtle.end_fill()

# draw left ear

turtle.left(180)
turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

# draw right ear

# move turtle
turtle.penup()
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
# draw circle

turtle.fillcolor("red")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.left(90)


screen.exitonclick()
