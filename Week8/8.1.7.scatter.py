# 8.1.7.scatter.py
# Program that makes a list called ages that has the same number random values as salaries(range:21 to 65)
# Make a scatter plot
# author Grainne Boyle

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberofEntries = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary,numberofEntries)
ages = np.random.randint(low=21, high =65, size = numberofEntries) # Andrew does not like this, he prefers having absolute values set at the top

plt.scatter(ages,salaries) # this will be random
plt.show()