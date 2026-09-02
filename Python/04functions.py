def my_function():
    print("Hello from a function")

#my_function()

def fahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(fahrenheitToCelsius(50))

# RETURN VALUES
def getGreeting():
    return "Hello from a function"

#message = getGreeting()
#print(message)
print(getGreeting())

# PASS STATEMENT
def notFunction():
    pass

# FUNCTION ARGUMENTS

def my_function(fname):
    print(fname + " Monreal")

my_function("Frederick")    

# PARAMETERS VS ARGUMENTS
def nameFunction(name):     # Name is a parameter
    print("Hello", name)

nameFunction("Frederick")   # "Frederick" is an argument

# NUMBER OF ARGUMENTS
def argFunction(fname, lname):
    print(fname + " " + lname)

argFunction("Frederick", "Monreal")

# DEFAULT PARAMETER VALUE
def countryFunc(country = "Norway"):
    print("I am from " + country)

countryFunc("Sweden")
countryFunc("India")
countryFunc()
countryFunc("Brazil")

# KEYWORD ARGUMENTS
def animalFunc(animal, name):
    print("I have a", animal)
    print("My", animal, "is named", name)

# Calling the function with keyword arguments
animalFunc(animal="cat", name="Whiskers")
# POSITIONAL ARGUMENTS
animalFunc("dog", "Buddy")
# MIXING POSITIONAL AND KEYWORD ARGUMENTS
animalFunc("parrot", name="Polly")

# DIFFERENT DATA TYPES
def fruitFunc(fruits):
    for fruit in fruits:
        print(fruit)

fruits = ["apple", "banana", "cherry"]
fruitFunc(fruits)

def personFunc(person):
    print("Name:", person["name"])
    print("Age:", person["age"])
    print("City:", person["city"])

person = {"name": "John", "age": 30, "city": "New York"}
personFunc(person)

# RETURN VALUES
def numFunction(x, y):
    return x + y

result = numFunction(5, 3)
print(result)

# RETURNING DIFFERENT DATA TYPES
def diffFunc():
    return (10, 20)

x, y = diffFunc()
print("x:", x)
print("y:", y)

# POSITIONAL-ONLY ARGUMENTS

#def posOnlyFunc(name, /):
def posOnlyFunc(name):
    print("Hello", name)

#posOnlyFunc("Frederick")
posOnlyFunc(name="Frederick")  # This will raise an error if the function is defined with positional-only arguments

# KEYWORD-ONLY ARGUMENTS
#def kwOnlyFunc(*, name):
def kwOnlyFunc(name):
    print("Hello", name)

#kwOnlyFunc(name="Frederick")  # This works
kwOnlyFunc("Frederick")  # This will raise an error if the function is defined with keyword-only arguments

# COMBINING POSITIONAL-ONLY AND KEYWORD-ONLY ARGUMENTS
def combinedFunc(a, b, /, *, c,d ):
    return a + b + c + d

result = combinedFunc(5, 10, c=15, d=20)
print(result)

# ARBITRARY ARGUMENTS
def arbitraryFunc(*kids):
    print("The youngest child is ", kids[2])

arbitraryFunc("Emil", "Tobias", "Linus")

# ARGUMENTS
def argsFunc(*args):
    print("Type", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All argument:", args)

argsFunc("Frederick", "Armena", "Monreal")

def regArgs(greeting, *names):
    for name in names:
        print(greeting, name)

regArgs("Hello", "Frederick", "Armena", "Monreal")

def numArgs(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(numArgs(1, 2, 3))
print(numArgs(10, 20, 30, 40))
print(numArgs(5))

# KEYWORD ARGUMENTS
def keyArgs(**kid):
    print("His last name is ", kid["lname"])

keyArgs(name = "Tobias", lname = "Refsnes")

def info(**myvar):
    print("Type", type(myvar))
    print("Name", myvar["name"])
    print("Age:", myvar["age"])
    print("All data", myvar)

info(name = "Frederick", age = 17, city = "Bacacay")

def keyRegArgs(username, **details):
    print("Username", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)

keyRegArgs("4rmena", age = 25, city = "Bacacay", hobby = "coding")

# COMBINING ARGS & KWARGS
def combi(title, *args, **kwargs):
    print("Title", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

combi("User info", "Frederick", age = 17, city = "Bacacay")

# UNPACKING ARGUMENTS

def unFunction(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
result = unFunction(*numbers)
print(result)

# UNPACKING DICTIONARIES

def dictFunction(fname, lname):
    print("Hello", fname, lname)

person = {"fname": "Frederick", "lname": "Monreal"}
dictFunction(**person)

# SCOPE
def myfunc():
    x = 300
    print(x)

myfunc()

# FUNCTION INSIDE FUNCTION
def funcFunc():
    x = 300
    def innerFunc():
        print(x)
    innerFunc()

funcFunc()

# GLOBAL SCOPE

x = 300

def gsFunc():
    x = 200
    print(x)

gsFunc()

print(x)

# GLOBAL KEYWORD

def gkFunc():
    global x
    x = 300

gkFunc()

print(x)

# NONLOCAL KEYWORD

def nonLocalFunc():
    x = "Jane"
    def func2():
        nonlocal x
        x = "hello"
    func2
    return x

print(nonLocalFunc())

# LEGB RULE

x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner:", x)
    inner()
    print("Outer:", x)
outer()
print("Global:", x)