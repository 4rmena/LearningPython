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
gpa = 3.4
satScore = 1400
scholarship = "STEM"
familyIncome = 45000

if (scholarship == "STEM" or familyIncome < 50000) and gpa >= 3.5 and satScore >= 1400:
	print("You are eligible for the scholarship!")
elif satScore < 1400:
	print("You are not eligible for the scholarship due to low SAT score.")
elif gpa < 3.5:
	print("You are not eligible for the scholarship due to low GPA.")
elif familyIncome >= 50000:
	print("You are not eligible for the scholarship due to high family income.")
elif scholarship != "STEM":
	print("You are not eligible for the scholarship due to not being in the STEM field.")

# A4
initialH = 0
initialV = 30
time = 2
gravity = -9.8

height = initialH + (initialV * time) + (0.5 * gravity * (time ** 2))

if height >= 100:
	print("High altitude")
elif height > 5 and height < 100:
	print("In flight")
elif height <= 5:
	print("Near ground")
elif height < 0:
	print("Invalid, below ground level")
elif height == 0:
	print("Landed")

# A5
celsius = -41
fahrenheit = (celsius * 9/5) + 32

print(f"Temperature in Fahrenheit: {fahrenheit}F")

if fahrenheit > 86:
	print("Hot")
elif fahrenheit >= 77:
	print("Warm")
elif fahrenheit >= 32:
	print("Cool")
elif fahrenheit >= -40:
	print("Cold")
elif fahrenheit < -40:
	print("Extremely cold")