# 8.1.2.salaries.py
# Program that makes a list, that has 10 random numbers between 20000 and 80000
# author Grainne Boyle
# continuation of program adding new elements
# modify the program so that the random salaries are the same each time
import numpy as np
# it is a good idea to have your absolute value set into variables at the beginning of your program

minSalary = 20000
maxSalary = 80000
numberofEntries = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary,numberofEntries)
print (salaries)