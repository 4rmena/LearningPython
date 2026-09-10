# CHALLENGE 1

launch = (0, 0, 0)
orbit = (1000, 2000, 3000)
apogee = (1500, 2500, 3500)

print(launch)
print(orbit)
print(apogee)

print()

print(f"Y coordinates: {orbit[1]}")
print(f"Z coordinates: {apogee[2]}")

print()

if 1000 in orbit:
    print("Is 1000 in Position 2? Yes")
else:
    print("Is 1000 in Position 2? No")

if 5000 in apogee:
    print("Is 5000 in Position 3? Yes")
else:
    print("Is 5000 in Position 3? No")

print()

x = ("apogee",)
print(x)
print(type(x))

print()

y = ()
print(y)
print(type(y))

print()

# CHALLENGE 2
telemetry = ("500", "600", "700", "800")
print(f"Original telemetry: {telemetry}")

updatedTel = list(telemetry)
updatedTel[1] = 750

print(f"Updated telemetry (list): {updatedTel}")

newTel = tuple(updatedTel)
print(f"Updated telemetry (Tuple): {newTel}")

updatedTel = list(newTel)
updatedTel.append(850)

newTel = tuple(updatedTel)
print(f"New reading data: {newTel}")

removeTel = list(newTel)
removeTel.remove('500')
newUpdatedReading = tuple(removeTel)
print(f"Newly updated data: {newUpdatedReading}")

print()

# Mission Data Structure

def dataStructure(stage1, stage2, stage3):
    stages = [stage1, stage2, stage3]
    totalMass = 0
    totalBurnTime = 0
    highestTemp = 0

    for names, masses, times, temps in stages:
        print(f"Stage: {names}, Mass: {masses}kg, Burn Time: {times}s, Max Temp: {temps}K")
        totalMass += masses
        totalBurnTime += times
        if temps > highestTemp:
            highestTemp = temps

    print()

    return stages, totalMass, totalBurnTime, highestTemp

stage1 = ("Booster", 150, 60, 800)
stage2 = ("First Stage", 120, 90, 900)
stage3 = ("Second Stage", 100, 120, 950)

stages, totalMass, totalBurnTime, highestTemp = dataStructure(stage1, stage2, stage3)
print(f"Total Mission mass: {totalMass}")
print(f'Total Burn Time: {totalBurnTime}')
print(f"Highest Temperature reached: {highestTemp}")

print()

print(stages)
print(len(stages))

print()

mission_list = [stage1, stage2, stage3]
mission_list[0] = ("NewStage", 200, 70, 850)  # This works!
print(mission_list[0])