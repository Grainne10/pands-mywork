# 8.1.10.prettier-plot.py
# Program that makes a list called ages that has the same number random values as salaries(range:21 to 65)
#Add a line to this plot that shows y=x²
# Make a scatter plot
# author Grainne Boyle

import numpy as np
import matplotlib.pyplot as plt

minSalary = 20000
maxSalary = 80000
numberofEntries = 10

np.random.seed(1)
salaries = np.random.randint(minSalary, maxSalary,numberofEntries)
ages = np.random.randint(low=21, high =65, size = numberofEntries) 
plt.scatter(ages,salaries) # this will be random
#plt.show() if you do this the program will halt here until the plot is closed

# add x squared
xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints #multiply each entry by itself
plt.plot(xpoints,ypoints, color='r', label = "x squared")
plt.title('Random plot')
plt.xlabel("Salaries")
plt.ylabel("age")
plt.legend()

#plt.show() # see how the axis have changed
plt.savefig('prettier-plot.png')
