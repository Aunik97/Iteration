#Aunik Hussain
#Iteration Spotcheck


number = 0
total = 0
while number != -1:
    number = int(input("Please enter a number"))
    total = total + (number * number)
if number == -1:
    print("the total is", total)
