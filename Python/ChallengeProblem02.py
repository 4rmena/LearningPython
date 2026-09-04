# A1
c = 4

while c > 0:
    c -= 1
    print(c)

    if c == 0:
        print("LAUNCH")

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