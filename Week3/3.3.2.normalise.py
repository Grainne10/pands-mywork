# 3.3.2.normalise.py  
# This program reads in strings and strips
# any leading or trailing spaces.
# It also converts all the letters to lower case.
# It then outputs the lengths of the original string and the normalised one
# Author: Grainne Boyle

rawString = input('please enter a string: ')
normalisedString = rawString.strip().lower()

lengthofrawString = len(rawString)
lengthofnormalisedString = len(normalisedString)

print(f"That String normalised is : {normalisedString}")
print(f"we reduced the input string from {lengthofrawString} tto {lengthofnormalisedString} characters")