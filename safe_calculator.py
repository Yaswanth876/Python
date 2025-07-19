print("------SAFE CALCULATOR------")
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    op = input("Enter the operator (+, -, *, /): ")

    if op == '+':
        print(f"Sum of {num1} and {num2} is {num1 + num2}")
    elif op == '-':
        print(f"Difference of {num1} and {num2} is {num1 - num2}")
    elif op == '*':
        print(f"Product of {num1} and {num2} is {num1 * num2}")
    elif op == '/':
        print(f"Quotient of {num1} and {num2} is {num1 / num2}")
    else:
        print("❌ Invalid operator! Please use +, -, *, or /")

except ValueError:
    print("❌ Invalid input! Please enter numbers only.")
except ZeroDivisionError:
    print("❌ Division by zero is not allowed!")
