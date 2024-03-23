# 8.1.3.salaries.py
# Program that makes a list, that has 10 random numbers between 20000 and 80000
# author Grainne Boyle
# continuation of program adding new elements
# modify the program to make another array of numbers that has the salaries plus 5000

import numpy as np


minSalary = 20000
maxSalary = 80000
numberofEntries = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary,numberofEntries)
print (salaries)
salariesPlus = salaries + 5000 
# this will add 5000 to each value
print(salariesPlus)
