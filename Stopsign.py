#Kevin Collura
#CS-175L
#Turtle Graphics Stop Sign
import turtle


length=200
angle=45



turtle.penup()
turtle.goto(-100,242)
turtle.pendown()

turtle.pensize(20)
turtle.color("black", "red")
turtle.begin_fill()
for x in range(8):
    turtle.pendown()
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()

turtle.penup()
turtle.goto(-175,-75)
turtle.color("white")
turtle.write("STOP",font=("Arial", 105))
