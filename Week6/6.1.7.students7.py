# 6.1.6.students6.py
# Combine program for students and modules
# author Grainne Boyle

# week 7 - add the savedict()function into the file below
import json
# the array we store everything in
students = []
FILENAME ="students.json"
def writeDict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj,f)



def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(s) save students")
    print("\t(q) Quit")
    choice = input("Type one letter (a,v,q):").strip()
    return choice

def doAdd(students):
    currentStudent = {}
    currentStudent["name"] = input("Enter name : ")
    currentStudent["modules"] = readModules()
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :") .strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        # I am not doing error handling
        module["grade"] = int(input("\t\tEnter grade:"))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit) :").strip()
    return modules

def displayModules(modules):
    print("\tName  \tGrade")
    for module in modules:
        print("\t{}  \t{}".format(module["name"], module["grade"]))


def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"]);

def doSave():
    writeDict(students)
    print("students saved")



# main program
students = []

choice = displayMenu()
while(choice !='q'):
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice == 's':
        doSave()
    elif choice != 'q':
        print("\n\nplease select a,v or q")
    choice = displayMenu()