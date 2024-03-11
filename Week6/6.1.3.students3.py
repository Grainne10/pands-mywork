# 6.1.3.students.py
# Program that reads in the student's name, modules and grades. You want to see if the function works before adding it to your other functions.
# author Grainne Boyle

students= []
def readModules() :
    return []
def doAdd(students) :
    currentStudent = {}
    currentStudent["name"]=input("enter name :  ")
    currentStudent["modules"]=readModules()

    students.append(currentStudent)
#test
doAdd(students)

doAdd(students)

print (students)
