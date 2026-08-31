# A1
import random

age = random.randrange(14, 22)

if age >= 18:
    print("You can Drive now!")
else:
    print("You are not legally allowed to drive yet")

# A2
number = random.randrange(-5, 5)

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is 0")

# A3
grade = random.randrange(60, 100)

if grade >= 90:
    print("Letter grade: A")
elif grade >= 80:
    print("Letter grade: B")
elif grade >= 70:
    print("Letter grade: C")
else:
    print("Letter grade: F")