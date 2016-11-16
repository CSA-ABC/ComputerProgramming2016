#Elijah Mitchell
#Period 2
#9/2/16
print("Welcome to the hour teller!")
x=input("What time, in hours, is it?")
time=int(x)
y=input("How many hours till the alarm?")
alarm=int(y)
timediff=(wake%24)
end=(str(time+alarm))
print("The alarm will go off at "+end+".")
