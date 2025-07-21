import re

password = input("Enter your password: ")

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*])[A-Za-z\d@#$%^&*]{8,}'

if re.match(pattern, password):
    print(f"{password} is valid password")
else:
    print(f"{password} is invalid password")