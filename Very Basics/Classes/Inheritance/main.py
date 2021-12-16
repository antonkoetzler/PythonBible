from classes import *

var1 = Parent()
var1.print()
print()

var2 = Child1()
var2.print()
print()

var3 = Child2()
var3.print()
print("Using inherited Parent function parentFunc: ", end="", flush=True)
var3.parentFunc()
print()

var4 = Child4()
var4.print()
print("Using inherited Parent function parentFunc: ", end="", flush=True)
var4.parentFunc()
