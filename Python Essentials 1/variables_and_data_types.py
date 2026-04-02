"""PE1 Topic 2: Variables & Data Types"""

age = 21                # int
height = 5.9            # float
name = "Aisha"          # str
is_student = True       # bool

print(type(age), age)
print(type(height), height)
print(type(name), name)
print(type(is_student), is_student)

# Type casting
age_as_float = float(age)
height_as_int = int(height)
age_as_text = str(age)

print(age_as_float, type(age_as_float))
print(height_as_int, type(height_as_int))
print(age_as_text, type(age_as_text))
