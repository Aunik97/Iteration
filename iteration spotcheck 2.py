#Aunik Hussain
#Iteration Spotcheck Q2

count = 0
for count in range(1,12):
    count = count + 1
    number = int(input("Please enter an integer"))
answer = count * number    
print("{0:<2} * {1:<2} is {2:<2} ".format(count, number, answer))
