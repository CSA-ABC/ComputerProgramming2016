# Elijah Mitchell
# 10/14/16
# period 2
# globals
NAME = ""
PLANET = ""
CODE = 0
MIN = 0
MAX = 0
POINTS = 0
TOTAL = 0


def start():
    # sets how fast your going
    global NAME
    global PLANET
    print("Welcome " + NAME + " to planet " + PLANET + ".")
    speed = float(input("What is the speed you want to go at in Miles-Per-Second?\n"))
    escape_equation(speed)


def escape_equation(speed):
    # escape determination and counts up your points
    global MIN
    global MAX
    global POINTS
    global TOTAL
    if speed >= MAX:
        print("You went to fast and blew up!")
        print("Here are all the points you collected:")
        print(TOTAL)
        menu()
    elif speed <= MIN:
        print("You went to slow and crashed back down!")
        print("Here are all the points you collected:")
        print(TOTAL)
        menu()
    else:
        print("You have escaped the planet!")
        print("This is the planet " + PLANET + "'s code:")
        print(CODE)
        print("Here are your points:")
        print(POINTS)
        TOTAL = TOTAL + POINTS
        planet_picker()


def planet_picker():
    # lets you set destination
    # cant figure out how to make it where it doesnt let you go to the same planet
    global PLANET
    PLANET = input("Please pick a planet out of Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune and Pluto"
                   "or you can quit the game.\n").lower()
    escape_velocity()


def escape_velocity():
    # determines the speed needed to escape planet
    global MIN
    global MAX
    global PLANET
    global CODE
    global POINTS
    if PLANET == "mercury":
        gravity = float(3.7)
        MIN = gravity * .3
        MAX = gravity * .5
        CODE = 1
        POINTS = 3
        start()
    elif PLANET == "venus":
        gravity = float(8.87)
        MIN = gravity * .3
        MAX = gravity * .5
        CODE = 2
        POINTS = 4
        start()
    elif PLANET == "earth":
        gravity = float(9.8)
        MIN = gravity * .3
        MAX = gravity * .5
        CODE = 3
        POINTS = 5
        start()
    elif PLANET == "mars":
        gravity = float(3.7)
        MIN = gravity * .3
        MAX = gravity * .5
        CODE = 4
        POINTS = 3
        start()
    elif PLANET == "jupiter":
        gravity = float(24.79)
        MIN = gravity * .3
        MAX = gravity * .5
        CODE = 5
        POINTS = 7
        start()
    elif PLANET == "saturn":
        gravity = float(10.44)
        MIN = gravity * .3
        MAX = gravity * .5
        CODE = 6
        POINTS = 6
        start()
    elif PLANET == "uranus":
        gravity = float(8.69)
        MIN = gravity * .3
        MAX = gravity * .5
        CODE = 7
        POINTS = 5
        start()
    elif PLANET == "neptune":
        gravity = float(11.15)
        MIN = gravity * .3
        MAX = gravity * .5
        CODE = 8
        POINTS = 7
        start()
    elif PLANET == "pluto":
        print("Sorry this planet is no accessible due to the low gravity causing an untold amount of crashes.")
        planet_picker()
    elif PLANET == "quit":
        print("Quiting to menu...Points collected.")
        print(TOTAL)
        menu()
    else:
        print("That planet is not accepted.")
        planet_picker()
        # max speed is 50% more than escape speed
        # min speed is 10% times itself


def planet_codes(code):
    # planet codes
    global PLANET
    if code == 1:
        PLANET = "mercury"
        escape_velocity()
    elif code == 2:
        PLANET = "venus"
        escape_velocity()
    elif code == 3:
        PLANET = "earth"
        escape_velocity()
    elif code == 4:
        PLANET = "mars"
        escape_velocity()
    elif code == 5:
        PLANET = "jupiter"
        escape_velocity()
    elif code == 6:
        PLANET = "saturn"
        escape_velocity()
    elif code == 7:
        PLANET = "uranus"
        escape_velocity()
    elif code == 8:
        PLANET = "neptune"
        escape_velocity()
    elif code == 9:
        PLANET = "pluto"
        escape_velocity()
    else:
        print("Code incorrect.")
        menu()


def name():
    # name setter and set you on earth
    global NAME
    global PLANET
    NAME = input("So, what is the name of our Explorer?\n")
    PLANET = "earth"
    escape_velocity()


def intro():
    # literally the name
    print("Hello and welcome to the Space Explorer. You can buy your very own Space-Ship to travel across the universe!")
    name()


def menu():
    # again the name
    global TOTAL
    TOTAL = 0
    print("Please pick an option below using the numbers.")
    x = int(input("1.Start Game "
                  "2.Planet Code "
                  "3.End Game\n"))
    if x == 1:
        print("Loading new game...")
        intro()

    elif x == 2:
        code = int(input("Please enter the code.\n"))
        planet_codes(code)
    elif x == 3:
        print("Ending game...")
        quit(1)
    else:
        print("This is not an available choice.")
        menu()


menu()
