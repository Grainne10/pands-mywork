#  4.2.3.guess2.py 
 
# Program that prompts the user to guess a number, tells the user if their guess is too high or too low.
# author Grainne Boyle
import random
numberToGuess = 30
guess = random.randint(20,35)
print("here is a random number {}".format(guess))
while guess != numberToGuess:
    print("Incorrect, please try again")
    guess = numberToGuess
     # if the random number is not 30 then it will keep guessing until it gives the correct result and output below
    print ("Well done! Yes the number was ", numberToGuess)
# is not resolved come back and try again
    