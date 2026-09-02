# WHILE LOOPS
i = 0
while i < 6:
    #print(i)
    i += 1
    #if i == 3:
        #break
        #continue
    #print(i)
#else:
    #print("i is no longer less than 6")


k = 0
while k < 6:
    k += 1
    if k == 3:
        continue
    #print(k)

# FOR LOOPS
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    #print(x)
    if x == "banana":
        #break
        continue
    #print(x)

# RANGE FUNCTION
for z in range(5, 30, 5):
    print(z)

# ELSE IN FOR LOOPS
for y in range(6):
    if y ==3: break
    print(y)
else:
    print("Finally finished!")

 # NESTED LOOPS
adj = ["red", "big", "tasty"]

for x in adj:
    for y in fruits:
        print(x, y)

for j in [0, 1, 2]:
    pass

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)