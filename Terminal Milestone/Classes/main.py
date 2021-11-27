# from .BasicClass
from BasicClass import *
from Matrix import *

print()

foo = BasicClass(5)
print("Printing BasicClass object's data: ", end="", flush=True)
foo.printData()

print()

tree = Matrix(2)
print("Printing our matrix object")
tree.print()

print()
