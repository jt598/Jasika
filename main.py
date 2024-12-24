import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")

bend_turtle = turtle.Turtle()
bend_turtle.shape("turtle")
bend_turtle.color("black")

# Function to draw a bent line to the left
def draw_bent_line():
    bend_turtle.left(45) #it bends the line by 45
    bend_turtle.forward(50)#lenght of the line
    bend_turtle.left(45)#it 
    bend_turtle.forward(100)  # Move the turtle forward by 100 units
    bend_turtle.circle(15,180) #arch or semi circle
    bend_turtle.left(90)
    bend_turtle.penup()#it does not draw
   
    bend_turtle.forward(30)#the pen is moved to the right
    
    bend_turtle.pendown()# the pen can now draw
    bend_turtle.left(-270)
    bend_turtle.forward(35)
    bend_turtle.circle(19,180)
    bend_turtle.forward(100)
    bend_turtle.left(-45)#it put the pen in the 45 degree direction 
    #it doe not draw it 
    bend_turtle.forward(90)#it draws where the turtle.left says to draw

    bend_turtle.penup()
    bend_turtle.forward(-128)
    bend_turtle.pendown()
    bend_turtle.left(45)
    bend_turtle.forward(90)
    
# Move the turtle to the starting position
bend_turtle.penup()
bend_turtle.goto(-50, 0)
bend_turtle.pendown()

# Draw the bent line
draw_bent_line()


# Close the window on click
screen.exitonclick()
