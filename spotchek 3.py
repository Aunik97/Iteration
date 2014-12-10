#Aunik Hussain
#Iteration Spotcheck Q3

import random
number = random.randint(1,100)
NoTurn = 0

guess = int(input("enter your guess for the number"))
while guess == False:
    NoTurn = NoTurn + 1
    if guess == number:
        number == True
        print("well done youve guesssed correct")
    elif guess != number:
        print("Try again")
    


       
        
            
