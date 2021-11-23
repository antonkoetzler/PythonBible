# How to import everything from a file
from functions import *
# How to import specific things from a file
from information import bestActor, randomVariable

print("---Calling everything from functions.py---")
helloWorld()
print("\n")
helloMom()
print("\n")
helloYoutube()
print("\n")

print("---Calling everything we selected to import from information.py---")
bestActor()
print("\nrandomVariable: ", randomVariable)

# This would cause an error, since we didn't import it
# joke()
