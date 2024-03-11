# 6.1.1.students.py
# Program that creates new students and views students
# author Grainne Boyle

def displayMenu() :
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a,v,q) :").strip()
    return choice
def doAdd() :
    # we fill this in later
    print("in adding")
def doView() :
        # we fill this in later
    print("in viewing")

#main program
choice = displayMenu() 
while(choice != 'q') :
    if choice == 'a' :
        doAdd()
    elif choice == 'v' :
        doView()
    elif choice != 'q' :
        print("\n\nplease select a,v or q")
        choice=displayMenu()