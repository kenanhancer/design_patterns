numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(numbers)
print(fruits)

numbers.append(6)
fruits.append("fig")

print(numbers)
print(fruits)

numbers.insert(0, 0)
fruits.insert(0, "apricot")

print(numbers)
print(fruits)

numbers.extend([7, 8, 9])
fruits.extend(["grape", "honeydew", "kiwi"])

print(numbers)
print(fruits)

# Remove the first occurrence of the value 9
numbers.remove(9)
# Remove the first occurrence of the value "kiwi"
fruits.remove("kiwi")

print(numbers)
print(fruits)

# Remove the item at index 3
numbers.pop(3)
fruits.pop(3)

print(numbers)
print(fruits)

del numbers[2]
del fruits[2]

print(numbers)
print(fruits)

# List comprehension
squares = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]

print(squares)
print(evens)

# Check if a value is in a list
print(4 in numbers)
print("date" in fruits)

# Length of a list
print(len(numbers))
print(len(fruits))

squares_v2 = [x**2 for x in range(6)]
evens_v2 = [x for x in range(10) if x % 2 == 0]
words = ["apple", "banana", "cherry", "date", "elderberry"]
short_words = [word for word in words if len(word) < 6]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [number for row in matrix for number in row]
parity = ["even" if x % 2 == 0 else "odd" for x in range(10)]
pairs = [(x, x**2) for x in range(3)]
colors = ["red", "green", "blue"]
sizes = ["small", "medium", "large"]
combinations = [(color, size) for color in colors for size in sizes]
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
paired = [(x, y) for x, y in zip(list1, list2)]

for fruit in fruits:
    print(fruit)
