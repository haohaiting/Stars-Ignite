import turtle

# set up the windown
screen = turtle.Screen()
# ensure the size of the window will always be 300x500 ...
screen.setup(300, 500)

# background

# set the background color be red
screen.bgcolor("red")

# white dot background

# set the pencolor as white
turtle.pencolor('white')

# dot

# move turtle
turtle.penup()
turtle.goto(-100, 150)
turtle.pendown()

# draw circle
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

# dot

# move turtle
turtle.penup()
turtle.goto(150, 100)
turtle.pendown()

# draw circle
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

# dot

# move turtle
turtle.penup()
turtle.goto(-150, 50)
turtle.pendown()

# draw circle
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

# dot

# move turtle
turtle.penup()
turtle.goto(-50, -60)
turtle.pendown()

# draw circle
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

# dot

# move turtle
turtle.penup()
turtle.goto(-120, -100)
turtle.pendown()

# draw circle
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

# dot

# move turtle
turtle.penup()
turtle.goto(120, -100)
turtle.pendown()

# draw circle
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

# dot

# move turtle
turtle.penup()
turtle.goto(50, -140)
turtle.pendown()

# draw circle
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

# draw mickey

# set the pencolor as black
turtle.pencolor('black')

# draw face

# move turtle
turtle.penup()
turtle.goto(0, -60)
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
turtle.forward(100)
turtle.left(90)
turtle.forward(60)
turtle.right(180)
turtle.pendown()

# draw circle
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

# draw right ear

# move turtle
turtle.forward(120)

# draw circle
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()
# clikc to close the window after enjoying your mickey
screen.exitonclick()  
