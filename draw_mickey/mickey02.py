import turtle

# set up the windown
screen = turtle.Screen()
# ensure the size of the window will always be 300x500 ...
screen.setup(300, 500)

# make the turtle faster
turtle.speed(10)

# background

# set the background color be black
screen.bgcolor("black")

# draw mickey

# draw belly

# set the pencolor as red
turtle.pencolor('red')

# move turtle
turtle.penup()
turtle.goto(0, -1050)
turtle.pendown()

# draw circle
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(500)
turtle.end_fill()

# draw buttons

# set the pencolor as white
turtle.pencolor('white')

# move turtle
turtle.penup()
turtle.goto(-50, -150)
turtle.pendown()

# draw circle
turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# move turtle
turtle.penup()
turtle.goto(50, -150)
turtle.pendown()

# draw circle
turtle.fillcolor('white')
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()


# clikc to close the window after enjoying your mickey
screen.exitonclick()  
