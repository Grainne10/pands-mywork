# 4.1.2.grade.py 
 
# Program that reads in a student's percentage mark and prints out the corresponding grade
# author Grainne Boyle
percentage = float(input("Enter the percentage:"))

print (percentage)
if percentage < 0 or percentage > 100:
    print("please enter a number between 0 and 100")

elif percentage < 40: # we know it is greater than 0python 4.1.2.grade.py
    print("Fail")
elif percentage < 50: # we know it is between 40 and 49
    print("Pass")
elif percentage < 60: # we know it is between 50 and 59
    print("Merit1")
elif percentage < 70: # we know it is between 60 and 69
    print("Merit2")
else: #the only option left is between 70 and 100
    print("Distinction")


