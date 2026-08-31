# VARIABLES
x = 5              # x is of type int
x = "Wade"         # x is now of type str
y = "John"   

print(x)
print(y)

# TYPE VARIABLES
print(type(x))
print(type(y))

# VARIABLE NAMES
MyVariableName = "John"

# MULTIPLE VARIABLE
a, b, c = "Apple", "Banana", "Orange"
print(a, b, c)           # different printed variables

d = e = f = "Cherry"     # same value to multiple variables
print(d, e, f)           # same printed variables 

subjects = ["General Mathematics", "Physics", "Effective Communication"]
h, i, j = subjects
print(h, i, j)

# OUTPUT VARIABLES
x = 5
y = "John"
print(x, y)

# FUNCTION
ax = "awesome"

def myfunc():
  ax = "fantastic"
  print("Python is " + ax)

myfunc()

print("Python is " + ax)

# GLOBAL VARIABLES
bx = "awesome"

def myfunc1():
  global bx
  bx = "fantastic"
  print(bx)

myfunc1()

print("Python is " + bx)

"""
Inside the editor, complete the following steps:
Create a variable cx and assign it the value 5
Create a variable ay and assign it the value "John"
Use the type() function to print the type of cx
"""

cx = 5
ay = "John"
print(type(cx))