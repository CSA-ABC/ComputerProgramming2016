#Elijah Mitchell
#10/7/16
#period 2

def login_correct(x):
    print("Hi "+x)

def login_incorrect():
    incorrect+=1
    return incorrect
    if incorrect>=3:
        quit(1)

def login():
    name=input("What is your name?")
    pw='bob'
    entry=input("Password?")
    if pw==entry:
        login_correct(name)
    else:
        login_incorrect()
        login()
login()
