import turtle

def draw_mickey(turtle, position):
  turtle.penup()
  turtle.goto(position)
  turtle.pendown()
  
  draw_face(turtle)
  
  turtle.penup()
  turtle.left(90)
  turtle.forward(30)
  turtle.left(90)
  turtle.forward(20)
  turtle.right(180)
  turtle.pendown()
  
  draw_ear(turtle)
  
  turtle.forward(40)
  
  draw_ear(turtle)
  
  
def draw_face(turtle):
  turtle.fillcolor('white')
  turtle.begin_fill()
  turtle.circle(20)
  turtle.end_fill()
  
  
def draw_ear(turtle):
  turtle.fillcolor("white")
  turtle.begin_fill()
  turtle.circle(10)
  turtle.end_fill()
  

# set up the windown
screen = turtle.Screen()
# ensure the size of the window will always be 300x500 ...
screen.setup(300, 500)
# set the background color
screen.bgcolor("#da645a")
# make the turtle faster
turtle.speed(10)
# set turtle pensize
turtle.pensize(3)
# set turtle pencolor be black
turtle.pencolor("white")

# hardcode the positions for mickey(s)
positions = [(-120, 210), (0, 210), (120, 210),
             (-60, 120), (60, 120),
             (-120, 30), (0, 30), (120, 30),
             (-60, -60), (60, -60),
             (-120, -150), (0, -150), (120, -150),
             (-60, -240), (60, -240),]

# for every position in the positions list
for position in positions:
  # draw a mickey on that position
  draw_mickey(turtle, position)
  
screen.exitonclick()
