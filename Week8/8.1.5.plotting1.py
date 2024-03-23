# 8.1.5.plotting1.py
# Program that plots the function y = x²
# author Grainne Boyle

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints # multiply each entry by itself

plt.plot(xpoints, ypoints)
plt.show()