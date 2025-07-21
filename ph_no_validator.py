import re

phone = input("Enter your phone number: ")
pattern = r'^\d{10}$'

if re.match(pattern, phone):
    print(f"✅ {phone} is a valid phone number")
else:
    print(f"❌ {phone} is an invalid phone number")
