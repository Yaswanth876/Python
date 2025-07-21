import re

text = input("Paste a paragraph with emails: ")

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

emails = re.findall(pattern, text)
print("Extracted Emails:")
for email in emails:
    print("📧", email)
