#Elijah Mitchell
#9/9/16
#period 2
print("You are trying to get a table at a resturant for you and your date, but you have to be stylish enough to get in.")
print("Please enter a number between 0 and 10 to rate your stylishness.")
you = int(input("> "))
if you >= 1 and you <= 10:
    print("You have entered a valid number.")
else:
    print("You've entered an invailid number.")
print("Please enter a number between 0 an 10 to rate your date's stylishness.")
date=int(input("> "))
if date>=1 and date<=10:
    print("You have entered a vailid number.")
else:
    print("You have entered an invalid number.")
if you or date >=8:
    print("Congratulations on your date!")
elif you or date <8:
    print("you might get in!")
elif you or date >=5:
    print("You might get in!")
elif you or date <=2:
    print("You got kicked out.")
else:
    print("This is not vailid.")
