# 8.1.4.salaries.py
# Program that makes a list, that has 10 random numbers between 20000 and 80000
# author Grainne Boyle
# continuation of program adding new elements
# modify the program so that it increases all the salaries by 5%(store in another array)
import numpy as np


minSalary = 20000
maxSalary = 80000
numberofEntries = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary,numberofEntries)
print (salaries)
salariesMult = salaries * 1.05 
# this will add 5% by multiplying by 1.05
print(salariesMult)
newSalaries =salariesMult.astype(int)
print(newSalaries)