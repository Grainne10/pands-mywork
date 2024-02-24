#  4.2.5.average.py 
 
# Program that keeps reading numbers until the user enters a 0. 
# The program should then print out each of the numbers entered and the average of them.
# author Grainne Boyle

# This program reads in numbers until the user enters 0
# it will then print them bavk out again and their average
numbers = []
# first number then we check if it is 0 in the while loop
number = int(input("enter number (0 to quit) : "))
while number != 0:
    numbers.append(number)
        # read the next number and check if 0
    number = int(input("enter another (0 to quit): "))
for value in numbers:
    print (value)
    # I want average to be a float
average = float(sum(numbers)) / len (numbers)
print(f"The average is {average}")
