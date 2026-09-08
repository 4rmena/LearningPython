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
    excAlt = []

    for alt in data:
        if alt > highestAlt:
            highestAlt = alt
        if alt > 1000:
            excAlt.append(alt)
        if alt < lowestAlt:
            lowestAlt = alt


    return lowestAlt, highestAlt, len(excAlt)


data = [0, 100, 250, 500, 900, 1500, 2100, 2800]
data.append(3500)
print(f"Original readings: {data}")

data.pop(0)
print(f"Updated readings: {data}")

lowestAlt, highestAlt, excAlt = dashboard(*data)

print(f"Lowest Altitude: {lowestAlt}")
print(f"Highest Altitude: {highestAlt}")
print(f"Time altitude exceeded 1000m: {excAlt}")
print(f"Last 3 readings: {data[-3:]}")

print()

# SENSOR DATA PROCESSING 

def analyzeTemp(sensorA):
    max = sensorA[0]
    min = sensorA[0]


    for range in sensorA:
        if range > max:
            max = range
            print(max)
        if range < min:
            min = range

    range = max - min
    
    avgFloat = sum(sensorA) / len(sensorA)
    avgTemp = round(int(avgFloat), -1)



    return avgTemp, range
    

sensorA = [500, 550, 600, 650, 700]
sensorB = [520, 570, 620, 670]

print(f"Sensor A: {sensorA}")
print(f"Sensor B: {sensorB}")

sensorA.extend(sensorB)
print(f"Sensors Combined: {sensorA}")

sensorA.sort()
print(f"Sensors sorted: {sensorA}")

avgTemp, range = analyzeTemp(sensorA)
print(f"Average Temperature: {avgTemp}")
print(f"Range (Max - Min): {range}")

print()

# ORBITAL POSITIONS

print()

# ROCKET STAGE DATA
