# 5.2.1.queue.py
# Program that creates a queue and then takes one number out each time and leaves the others remaining until queue ends.
# author Grainne Boyle

student = {
    "name":"Mary",
    "modules": [
        {"courseName":"Programming",
         "grade": 45
         },
         { 
    "courseName":"History",
    "grade":99
         }
    ]
}
print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))