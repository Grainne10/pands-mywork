# 8.1.6.histogram.py
# Program that plots a histogram of the salaries 
# author Grainne Boyle

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberofEntries = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary,numberofEntries)
plt.hist(salaries)
plt.show()



