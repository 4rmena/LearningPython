# A1
import random

number = random.randrange(4, 10)

print(number)

if number % 2 == 0:
    print("Even!")
else:
    print("Odd!")

# A2
x = 0

while x < 20:
    x += 1
    if x == 9:
        continue

    if x % 3 == 0:
        print(x)

# A3
y = 0
while y < 5:
    y += 1

    def lists(y):
        return y + y

    