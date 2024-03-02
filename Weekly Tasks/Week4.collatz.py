#Week4collatz.py  
# Program asks user to read in a positive integer and outputs the successive values of the followin calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, multiply it by three and add one.
# Have the program end if the current value is one.
# author Grainne Boyle
import math
number = int(input("please enter a postive integer:"))
if (number % 2) == 0: 
    print (f"({number} * 2)")
       