#Aunik Hussain
#10/11/2014
#Guess The Number Programme

count = 0
import random
numbertoguess = random.randint(1,100)
while count != numbertoguess:
    number = int(input("please enter a number within the range 1 to 100"))
    count = count + 1
    if number > 100 or number < 1:
        count = count - 1
        print("please enter a number within the range")
    elif number < numbertoguess:
        print("The number is to low, try again")
    elif number > numbertoguess:
        print("number is too high")
    else:
        print("the number is correct it took you {0} attempts".format(count))
     
