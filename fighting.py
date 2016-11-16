#Elijah Mitchell
#9/29/16
#period 2


import random
name=input("What is your name? ")
print("Welcome "+name+"!")
defense=random.randrange(0,11)
print("Lookout "+name+"! Its the Killer Bunny Fred!")
KBF=int(random.randrange(5,11))
print("Hurry! Attack Fred!")
        
x=input("Pick an attack! Throw a fire, your sword or shoot it with an arrow!{Choices: Fire, Sword and Bow.} ")

if x==str('fire'):
    x=random.randrange(1,14)
    print("You fling a Fireball at Fred!")
elif x==str('sword'):
    x=random.randrange(0,9)
    print("Your sword sings through the air towards Fred.")
elif x==str('bow'):
    x=random.randrange(2,8)
    print("You fire an arrow that whistles like the wind towards Fred.")
    
print("Your Attack Damage: "+str(x))
print("Killer Bunny Fred's health: "+str(KBF))

if int(x)>KBF:
    print("YAY! You killed the Killer Bunny Fred, great job "+name+"!")
elif int(x)<KBF:
    print("You fought bravely but it was not enough to slay the deadly foe...")
elif int(x)==KBF:
    print("You have done the world a service by ridding the world of Fred but, you have fallen in battle.")
else:
    print("Ummmmm.... you broke it...")
