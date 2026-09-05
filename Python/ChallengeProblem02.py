# A1
#c = 4

#while c > 0:
#    c -= 1
#    print(c)

#    if c == 0:
#        print("LAUNCH")

for countdown in range(10 ,-1 ,-1):
    print(countdown)

    if countdown == 0:
        print("LAUNCH!")

# A2
def fuel(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(fuel(500, 300, 200))

# A3
Outer = [1, 2, 3, 4, 5]
Inner = [1, 2, 3, 4, 5]

for v in Outer:
    print(v, end=" ")
print()
for w in Inner:
    w *= 2
    print(w, end=" ")
print()
for x in Inner:
    x *= 3
    print(x, end=" ")
print()
for y in Inner:
    y *= 4
    print(y, end=" ")
print()
for z in Inner:
    z *= 5
    print(z, end=" ")
print()

# C3
for row in Outer:
    for col in Inner:
        print(row * col, end=" ")
    print()

# C4

def analyze_temps(temps):
    max_temp = temps[0]
    total = 0
    
    for temp in temps:
        if temp > max_temp:
            max_temp = temp
        total += temp
    
    avg_temp = total / len(temps)
    return max_temp, avg_temp

temps = [500, 750, 1200, 950, 800]
max_temp, avg_temp = analyze_temps(temps)
print(f"Max: {max_temp}, Average: {avg_temp}")

# A5
def orbit_simulator(position, velocity, time_steps):
    print(f"Time 0: {position} km")
    
    for second in range(1, time_steps + 1):
        position += velocity
        print(f"Time {second}: {position} km")
    
    return position

final = orbit_simulator(1000, 50, 10)
print(f"Final position: {final} km")