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
def sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9,10))