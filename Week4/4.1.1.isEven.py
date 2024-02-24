# 4.1.1.isEven.py 
 
# Program where user enters a number and the program will tell the user if the number is even or odd
# author Grainne Boyle

# If question is asking whether the number can be divided by 2 without a remainder then it is even, else oddpyh
number = int(input("enter an integer: "))
if (number % 2) == 0:
    print (f"{number} is an even number")
else:
    print(f"{number} is an odd number")
