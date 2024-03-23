# 8.1.1.salaries.py
# Program that makes a list, that has 10 random numbers between 20000 and 80000
# author Grainne Boyle

import numpy as np
# it is a good idea to have your absolute value set into variables at the beginning of your program
minSalary = 20000
maxSalary = 80000
numberofEntries = 10

salaries = np.random.randint(minSalary, maxSalary,numberofEntries)
print (salaries)