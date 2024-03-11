# 6.1.4.students4.py
# Continuation of program , you want to read in modules.
# author Grainne Boyle

def readModules() :
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :") .strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        # I am not doing error handling
        module["grade"]=int(input("\t\tEntergrade:"))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit) :").strip()
    return modules
