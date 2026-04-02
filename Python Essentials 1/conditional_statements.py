"""PE1 Topic 5: Conditional Statements"""

score = int(input("Enter your score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

# Nested condition example
if score >= 60:
    if score == 100:
        print("Perfect score!")
    else:
        print("You passed.")
else:
    print("You did not pass.")
