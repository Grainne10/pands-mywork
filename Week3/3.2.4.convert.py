## convert.py  
# Program converts takes in a float number and returs that number in cents
# author Grainne Boyle

number = float(input("Enter a number: "))
absoluteValue = abs(number*100)
print ('The absolute value of {} is {} '.format(number, absoluteValue))
