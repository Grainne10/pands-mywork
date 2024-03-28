# 9.1.2.useFib.py
# This program uses the module in the myfunctions program.
# It prompts the user for a number and will retunrn th elist of the Fibonacci sequence(remember to turn off the debug level 
# in the module by commenting out the line logging.basicConfig

import myFunctions

nTimes = int(input('how many:'))
print(myFunctions.fibonacci(nTimes))