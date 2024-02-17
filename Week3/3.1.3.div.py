# 3.1.3.div.py  
# Program reads two numbers and divides the first number by the second and gives the integer result and the remainder
# author Grainne Boyle

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))
answer = int(x//y) # // gives the int division
remainder = int(x%y) # % gives the remainder
print ("{} divided by {} is {} with remainder {}".format( x, y, answer, remainder))
