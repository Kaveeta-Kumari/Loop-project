numbers = []

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    numbers.append(num)

total = sum(numbers)
average = total / 10
largest = max(numbers)
smallest = min(numbers)

even = 0
odd = 0
for n in numbers:
    if n % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print(f"\n--- Result ---")
print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Number of even numbers: {even}")
print(f"Number of odd numbers: {odd}")