num = int(input("Enter the number: "))
print("----------------------------")
print(f"Multiplication Table of {num}")
print("----------------------------")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
