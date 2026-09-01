# A1
import random

carSpeed = random.randrange(25, 65)

if carSpeed >= 65:
	print("Speeding severe!")
elif carSpeed >= 55:
	print("Speeding mild!")
elif carSpeed >= 25:
	print("Normal speed.")
elif carSpeed <= 25:
	print("Too slow")

# A2
fuelLevel = random.randrange(98, 101)
weather = "Clear"
engineTempt = random.randrange(730, 850)
crewReady = True

if fuelLevel == 100:
	if weather == "Clear":
		if crewReady:
			if engineTempt > 850:
				print("Engine temperature too high!")
			elif engineTempt >= 750:
				print("Launch approved!")
			elif engineTempt < 750:
				print("Engine temperature too low!")
		else:
			print("Crew not ready!")
	else:
		print("Weather not clear!")
else:
    print("Fuel level not full!")

# A3
