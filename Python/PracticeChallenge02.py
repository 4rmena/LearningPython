# A1
print("ANSWER 1")

def countdown():
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
    maxTemp = temps[0]
    total = 0

    for temp in temps:
        if temp > maxTemp:
            maxTemp = temp

        total += temp

    avgTemp = total / len(temps)
    return avgTemp, maxTemp


temps = [500, 750, 1200, 950, 800]
avgTemp, maxTemp = analyzeTemps(*temps)
print(f"Average: {avgTemp}, Max: {maxTemp}")

print()

# ORBITAL POSITION CALCULATOR
def orbitSimulator(pos, vel, time):
    print(f"Time: 0, Position: {pos}")

    for sec in range(1, time + 1):
        pos += vel
        print(f"Time: {sec}, Position: {pos}")

    return pos

final = orbitSimulator(1000, 50, 10)
print(f"Final Position: {final}")   

# ROCKET FUEL BURN
def fuelSim(fuel,burnRate, time):
    print(f"Time: 0, Fuel: {fuel}")

    for sec in range(1, time + 1):
        fuel -= burnRate
        print(f"Time: {sec}s, Fuel: {fuel}kg")

    return fuel

final = fuelSim(500, 20, 10)
print(f"Final fuel: {final}")

# ROCKET ALTITUDE
def altitudeSim(altitude, climbRate, time):
    print(f"Time: 0s, Altitude: {altitude}m")

    for sec in range(1, time + 1):
        altitude += climbRate
        print(f"Time: {sec}s, Altitude: {altitude}m")
    return altitude

final = altitudeSim(200, 75, 8)
print(f"Final Altitude: {final}m")