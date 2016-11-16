#Elijah Mitchell
#9/22/16
#period 2
import turtle
bob=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor('black')
bob.color('blue')
bob.speed(.00001)
bill=turtle.Turtle()
bill.speed(.00001)
bill.color('red')
for i in range(2000):
    bob.forward(i)
    bob.right(240)
    bill.forward(i)
    bill.right(241)


    
