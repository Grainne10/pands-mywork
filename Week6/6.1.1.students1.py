# 6.1.1.students1.py
# Program that creates new students and views students
# author Grainne Boyle

def displayMenu() :
    print("What would you like to do?")
    print("\t(a) Add new student")
# \t this tabs the line
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a,v,q) :").strip()

    return choice
# test the function
choice = displayMenu()
print(f"you chose { choice }")
