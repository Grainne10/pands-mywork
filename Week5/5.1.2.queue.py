# 5.2.1.queue.py
# Program that creates a queue and then takes one number out each time and leaves the others remaining until queue ends.
# author Grainne Boyle

import random
queue = []
numberofNumbers = 10
rangeTo = 100
for n in range(0,numberofNumbers):
    queue.append(random.randint(0,rangeTo))
print(f"[queue] is {queue}")
while len(queue) != 0:
    currentNumber = queue.pop(0)
#pop(0)takes the first number out of a list
    print (f"current Number is {currentNumber} and the queue is {queue}")
    # the missing piece of this was f to make it a function
print ("the queue is now empty")
