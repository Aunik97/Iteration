# Write a program that asks for a number and displays the squares
# of all the integers between 1 and this number inclusive.
# It should print 5 values on each line in neat columns.



    
count = -1 
number = int(input("please enter a number"))
while count <= number:
    count = count + 1
    if count <= number:
        total = (number - count )** 2
        print("{0}".format(total)
    else:
        print("programe end")
