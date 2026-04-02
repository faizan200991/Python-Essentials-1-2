"""PE2 Topic 7: Dictionaries & Tuples (Advanced)"""

student_scores = {"Ali": 88, "Sara": 93, "Omar": 79}

print("Keys:", list(student_scores.keys()))
print("Values:", list(student_scores.values()))
print("Items:", list(student_scores.items()))

for name, score in student_scores.items():
    print(f"{name}: {score}")

# Tuple unpacking
point = (4, 7)
x, y = point
print("Unpacked point:", x, y)
