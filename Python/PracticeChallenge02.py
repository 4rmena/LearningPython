# A1
print("ANSWER 1")

def countdown(*start):
    for start in range(10, -1, -1):
        print(start)
        if start == 0:
            print("LAUNCH!!!")

countdown()

print()

# A2
print("ANSWER 2")

def fuelAmount(*fuel):
    total = 0
    for fuelConsumption in fuel:
        total += fuelConsumption
    return total


total = fuelAmount(500, 300, 200)
print(fuelAmount(total))

print()

# A3
print("ANSWER 3")

outer = [1, 2, 3, 4, 5]
inner = [1, 2, 3, 4, 5]

for row in outer:
    print()
    for col in inner:
        print(row * col, end=" ")

print()

# A4
print("ANSWER 4")

def analyzeTemps(*temps):
    avgTemp = 0
    for avg in temps:
        avgTemp += avg

    maxTemp = temps[0]
    for max in temps:
        if max > maxTemp:
            maxTemp = max
    return avgTemp, maxTemp


temps = [500, 750, 1200, 950, 800]
avgTemp, maxTemp = analyzeTemps(*temps)
print(f"Average: {avgTemp}, Max: {maxTemp}")

print()