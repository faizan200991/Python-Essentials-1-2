"""PE1 Topic 7: Lists & List Operations"""

fruits = ["apple", "banana", "cherry"]
print("Original:", fruits)

# Indexing and slicing
print("First item:", fruits[0])
print("Slice [0:2]:", fruits[0:2])

# Add/remove
fruits.append("orange")
fruits.insert(1, "mango")
fruits.remove("banana")
print("After changes:", fruits)

# Iterating
for fruit in fruits:
    print("Fruit:", fruit)

# Functions
print("Length:", len(fruits))
print("Sorted:", sorted(fruits))
