fruits = ["apple", "banana", "cherry", "orange", 'kiwi', "melon", "grapes"]
numbers = (0, 1, 2, 3, 4)

fruits[0:1] = ["mango", "avocado"]
fruits.insert(0, "berry")
fruits.append("blue berry")
fruits.extend(numbers)
fruits.remove("banana")
fruits.pop(-1)
del fruits[0:1]
print(fruits)

def avgTemp(readings):
    print(sum(readings))
    return sum(readings) / len(readings)

engineTemp = [500, 550, 600, 650, 700]
avg = avgTemp(engineTemp)
print(f"Average temperature: {avg}")