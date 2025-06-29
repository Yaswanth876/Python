age = int(input("Enter your age: "))
if age<18:
    print("You're a Minor")
elif age>18 and age<60:
    print("You're an Adult")
else:
    print("You're a Senior")