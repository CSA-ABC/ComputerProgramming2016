#Elijah Mitchell
#9/28/16
#period 2
import random
p1=int(random.randrange(1,101))
p2=int(random.randrange(1,101))
print("Player 1 top, Player 2 bottom.")
print(p1)
print(p2)
if p1>p2:
    print("Player 1 wins!")
elif p1<p2:
        print("Player 2 wins!")
else:
    p1=p2
    print("Its a draw!")
