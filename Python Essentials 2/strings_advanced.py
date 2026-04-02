"""PE2 Topic 2: Strings (Advanced)"""

text = "  python essentials course  "

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Stripped:", text.strip())

words = text.strip().split()
print("Split words:", words)
print("Joined:", "-".join(words))

sentence = "I like Java"
updated = sentence.replace("Java", "Python")
print("Replaced:", updated)

name = "Sana"
score = 92.5
print(f"Student {name} scored {score}%.")
