#Guess the number
#Heather Amo
import random

r= random.randint(1,11)

guess=input("Guess a number between 1 and 10.")

g=int(guess)
print ("g1 "+str(g))
while g != r:
    if g > r:
        g=int(input(str(g)+ " is too high.  Try again."))
        print("g2 "+str(g))
    elif g<r:
        g = int(input(str(g) + " is too low.  Try again."))
        print("g3 " + str(g))
print ("Good job, you got the right answer!")