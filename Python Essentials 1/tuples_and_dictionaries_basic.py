"""PE1 Topic 9: Tuples & Dictionaries (Basic)"""

# Tuple (immutable)
coordinates = (10, 20)
print("Coordinates:", coordinates)
print("X:", coordinates[0])

# Dictionary (key-value)
student = {
    "name": "Ali",
    "age": 18,
    "course": "Python Essentials"
}

print("Student:", student)
print("Name:", student["name"])

# Basic operations
student["age"] = 19
student["city"] = "Lahore"
print("Updated:", student)
