#Elijah Mitchell
#9/28/16
#period 2
import random
name=input("What is your name?")
print("Hi "+name+"! Let's play the guessing game!")
x=random.randrange(1,100)
y=int(input("Please enter a number between 1 and 100."))
if y>x:
    print("YAY! You won "+name+"!")
elif y == x:
        print("Its a draw!")
else:
    y<x
    print("Sorry "+name+" you lose.")

print("Top is A.I.'s number and the bottom is your number.")
print(x)
print(y)
