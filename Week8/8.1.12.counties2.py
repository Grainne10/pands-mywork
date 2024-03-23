# 8.1.12.counties2.py
# Program that makes a list of counties
# Make a pie chart
# author Grainne Boyle

import numpy as np
import matplotlib.pyplot as plt

# make the array of occurences
possibleCounties = ['tyrone','Galway', 'Donegal', 'Derry', 'Sligo']
#pick 100 randomly from possible counties with the frequencies set in p
counties = np.random.choice(possibleCounties, p=[0.1,0.3,0.2,0.12,0.28], size=(100))
#now we need the occurences of each county 
# this returns a tuple of the unique values and how many times they appear
unique, counts =np.unique(counties, return_counts=True)
# we can put this into a pie plot
plt.bar(unique, counts)
plt.show()