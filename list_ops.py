n = int(input("Enter range: "))
numbers = []


for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

maximum = max(numbers)
minimum = min(numbers)
average = sum(numbers) / len(numbers)

print("------------------------")
print("Numbers Entered :", numbers)
print("Maximum Value   :", maximum)
print("Minimum Value   :", minimum)
print("Average         :", average)
print("------------------------")
