# EXAMPLE
def avgTemp(readings):
    print(sum(readings))
    return sum(readings) / len(readings)

engineTemp = [500, 550, 600, 650, 700]
avg = avgTemp(engineTemp)
print(f"Average temperature: {avg}")

print()

# MISSION CONTROL DASHBOARD

def dashboard(*data):
    highestAlt = data[0]
    excAlt = []

    for alt in data:
        if alt > highestAlt:
            highestAlt = alt
        if alt > 1000:
            excAlt.append(alt)

    return highestAlt, len(excAlt)


data = [0, 100, 250, 500, 900, 1500, 2100, 2800]
data.append(3500)
print(f"Original readings: {data}")

data.pop(0)
print(f"Updated readings: {data}")

highestAlt, excAlt = dashboard(*data)

print(f"Highest Altitude: {highestAlt}")
print(f"Time altitude exceeded 1000m: {excAlt}")
print(f"Last 3 readings: {data[-3:]}")

print()

# SENSOR DATA PROCESSING 

def analyzeTemp(sensorA):
    max = sensorA[0]
    min = sensorA[0]

    avgFloat = sum(sensorA) / len(sensorA)
    avgTemp = round(int(avgFloat), -1)

    for range in sensorA:
        if max < range:
            max = range
        if min > range:
            min = range

    range = max - min

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