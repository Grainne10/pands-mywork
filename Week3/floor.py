# floor.py  
# Program takes in a float and outputs an int rounded down
# author Grainne Boyle

# you need to import math module which is built in

import math

numbertofloor = float(input("Enter a float number: "))
flooredNumber = math.floor(numbertofloor)
print ('{} floored is {} '.format(numbertofloor, flooredNumber))