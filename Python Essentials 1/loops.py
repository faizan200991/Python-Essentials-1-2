"""PE1 Topic 6: Loops"""

print("While loop:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

print("\nFor loop:")
for i in range(1, 6):
    if i == 3:
        print("Skipping 3 with continue")
        continue
    if i == 5:
        print("Stopping at 5 with break")
        break
    print("i =", i)

print("\nPass example:")
for _ in range(2):
    pass
print("pass does nothing, but keeps syntax valid.")
