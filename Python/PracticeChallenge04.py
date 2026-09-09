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