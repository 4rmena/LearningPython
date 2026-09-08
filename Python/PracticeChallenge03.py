# EXAMPLE 00
def avgTemp(readings):
    print(sum(readings))
    return sum(readings) / len(readings)

engineTemp = [500, 550, 600, 650, 700]
avg = avgTemp(engineTemp)
print(f"Average temperature: {avg}")

print()

# EXAMPLE 01
fruits = ["apple", "banana", "cherry", "orange", 'kiwi', "melon", "grapes"]
numbers = (0, 1, 2, 3, 4)

# Do all your operations
fruits[0:1] = ["mango", "avocado"]
fruits.insert(0, "berry")
fruits.append("blue berry")
fruits.extend(numbers)
fruits.remove("banana")
fruits.pop(-1)
del fruits[0:1]

# NEW: Add analysis
print("Final list:", fruits)
print("Length:", len(fruits))
print("First item:", fruits[0])
print("Last item:", fruits[-1])
print("Items that are strings:", sum(1 for item in fruits if isinstance(item, str)))
print("Items that are integers:", sum(1 for item in fruits if isinstance(item, int)))

print()

# MISSION CONTROL DASHBOARD

def dashboard(*data):
    highestAlt = data[0]
    lowestAlt = data[0]
#    excAlt = []

    for alt in data:
        if alt > highestAlt:
            highestAlt = alt
#        if alt > 1000:
#            excAlt.append(alt)
        if alt < lowestAlt:
            lowestAlt = alt

    highAlt = [x for x in data if x > 1000]

#    return lowestAlt, highestAlt, len(excAlt)
    return lowestAlt, highestAlt, highAlt

data = [0, 100, 250, 500, 900, 1500, 2100, 2800]
data.append(3500)
print(f"Original readings: {data}")

data.pop(0)
print(f"Updated readings: {data}")

# lowestAlt, highestAlt, excAlt = dashboard(*data)
lowestAlt, highestAlt, highAlt = dashboard(*data)

print(f"Lowest Altitude: {lowestAlt}")
print(f"Highest Altitude: {highestAlt}")
# print(f"Time altitude exceeded 1000m: {excAlt}")
# Alternative for last 3 readings
print(f"Times altitude exceeded 1000m: {len(highAlt)}")
print(f"Last 3 readings: {data[-3:]}")

print()

# SENSOR DATA PROCESSING 
def analyzeTemp(sensorA):
    max = sensorA[0]
    min = sensorA[0]

    for temp in sensorA:
        if temp > max:
            max = temp
        if temp < min:
            min = temp
    temp = max - min
    
    avgFloat = sum(sensorA) / len(sensorA)
    avgTemp = round(avgFloat, 0)

    return avgTemp, temp
    
sensorA = [500, 550, 600, 650, 700]
sensorB = [520, 570, 620, 670]
print(f"Sensor A: {sensorA}")
print(f"Sensor B: {sensorB}")

sensorA.extend(sensorB)
print(f"Sensors Combined: {sensorA}")

sensorA.sort()
print(f"Sensors sorted: {sensorA}")

avgTemp, temp = analyzeTemp(sensorA)
print(f"Average Temperature: {avgTemp}")
print(f"Range (Max - Min): {temp}")

"""
Errors:
Variable naming (shadowing built-ins)
Rounding logic could be clearer
"""

print()

# ORBITAL POSITIONS

def posCoords():
    x = posDataB[0] - posDataA[0]
    y = posDataB[1] - posDataA[1]
    z = posDataB[2] - posDataA[2]

    return x, y, z
    

posDataA = [1000, 2000, 3000]
posDataB = [1050, 2100, 3100]

X, Y, Z = posCoords()

print(f"Distance in X: {X}")
print(f"Distance in Y: {Y}")
print(f"Distance in Z: {Z}")


print()

# ROCKET STAGE DATA

def stageData():
    longestBurn = burnTimes[0]
    total = 0

    for long in burnTimes:
        if long > longestBurn:
            longestBurn = long

        total += long
        # BUG: Changed from longestBurn to long

    return longestBurn, total

stage = (1, 2, 3)
mass = (150, 120, 100)
burnTimes = (60, 90, 120)

data = [stage, mass, burnTimes]
x, y, z = map(list, zip(*data))

longestBurn, total = stageData()

print(f"Stage 1: {x}")
print(f"Stage 2: {y}")
print(f"Stage 3: {z}")
print(f"Total mass: {sum(mass)}")
print(f"Total burn time: {total}")
print(f"Longest burn: {longestBurn}")