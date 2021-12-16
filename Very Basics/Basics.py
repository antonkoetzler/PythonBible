# Very basics to python
# This is how you make a comment

# Variables
a = 5 # Creating a variable
b = a + 5

# Basic printing
print("Hello World")

print("\nHere are some variables I made:")
print("   a: ", a)
print("   b: ", b)

# For loop
print("\n")
for x in range(5):
    print("This is a basic for loop in python, iteration: ", x)

# White loop
print("\n")
while a != 0:
    print("This is a basic while loop in python, iteration: ", a)
    a -= 1

# Arrays
print("\n")
arr = []

print("This is my array's length: ", len(arr))

for x in range(5):
  arr.append(x);

print("This is my array's length after inserting values: ", len(arr))

print("\nMy array's values")
for x in range(5):
  print(arr[x])
