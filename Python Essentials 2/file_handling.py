"""PE2 Topic 4: File Handling"""

file_name = "sample_notes.txt"

# Write mode (w): create/overwrite
with open(file_name, "w", encoding="utf-8") as file:
    file.write("Python file handling practice\n")
    file.write("Second line\n")

# Append mode (a): add to end
with open(file_name, "a", encoding="utf-8") as file:
    file.write("Appended line\n")

# Read mode (r): read content
with open(file_name, "r", encoding="utf-8") as file:
    print("Full content using read():")
    print(file.read())

with open(file_name, "r", encoding="utf-8") as file:
    print("First line using readline():", file.readline().strip())
