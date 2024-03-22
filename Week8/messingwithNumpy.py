# Messing with numpy
# Author: Grainne Boyle
import numpy as np

list_of_numbers=[1,2,3,"asdf"]
print (list_of_numbers)

numbers = np.array([1,2,3,4])
numbers = numbers * [1,2,3,5]
print ('array',numbers) 

rando = np.random.randint(100,200,30)
print(rando)