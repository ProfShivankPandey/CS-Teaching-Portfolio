# Control Flow: Conditionals
score = 82

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C"

print(f"Assigned Grade: {grade}")

# Control Flow: Loops (Iterating over a range)
print("\nCountdown loop:")
for i in range(3, 0, -1):
    print(i)
print("Launch!")