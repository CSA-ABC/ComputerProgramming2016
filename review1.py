#Elijah Mitchell
#9/19/16
#period 2
sides=int(input("Please enter the number of sides."))
length=int(input("Please enter the length of the sides."))
angle=int(input("Please enter the angle of the turns."))
col=input("Please enter the name of a color.")
import turtle
bob=turtle.Turtle()
fillcolor('col')
for i in range(sides):
    bob.forward(length)
    bob.right(angle)
end_fill()
