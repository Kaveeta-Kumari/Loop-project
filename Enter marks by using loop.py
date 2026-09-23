total = 0

for i in range(1, 6):
    marks = int(input(f"Enter marks of Subject {i}: "))
    total = total + marks

percentage = total / 5

print("\n--- Result ---")
print("Total Marks:", total)
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Grade: A+")
elif percentage >= 70:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
else:
    print("Grade: F")

if percentage >= 33:
    print("Status: Pass")
else:
    print("Status: Fail")