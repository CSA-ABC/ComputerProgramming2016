# Elijah Mitchell
# period 2
# 11/15/16

def math(num):
    x = int(num)
    if x % 2 == 0:
        a = (x/2)
        print(a)
    else:
        print("This does not compute...")
    y = int(num)
    if y % 5 == 0:
        b = (y/5)
        print(b)
    else:
        print("This does not compute...")
    z = int(num)
    if z % 6 == 0:
        c = (z/6)
        print(c)
    else:
        print("This does not compute...")


number = int(input("Please enter the number you wish to test.\n"))
math(number)
