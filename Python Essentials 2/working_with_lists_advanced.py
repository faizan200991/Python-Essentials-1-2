"""PE2 Topic 6: Working with Lists (Advanced)"""

numbers = [5, 1, 8, 2, 9, 3]

# List comprehension: squares of even numbers
even_squares = [n ** 2 for n in numbers if n % 2 == 0]
print("Even squares:", even_squares)

# Nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("Matrix rows:")
for row in matrix:
    print(row)

# Sorting techniques
print("Sorted ascending:", sorted(numbers))
print("Sorted descending:", sorted(numbers, reverse=True))
