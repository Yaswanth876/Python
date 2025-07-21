import re

def extractor(text):
    # 🔧 Regex patterns
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    phone_pattern = r'\b\d{10}\b'
    date_pattern = r'\b\d{2}-\d{2}-\d{4}\b'

    # 📨 Extract emails
    emails = re.findall(email_pattern, text)
    print("\n📧 Extracted Emails:")
    for email in emails:
        print("   ➤", email)

    # 📞 Extract phone numbers
    phones = re.findall(phone_pattern, text)
    print("\n📱 Extracted Phone Numbers:")
    for phone in phones:
        print("   ➤", phone)

    # 📅 Extract dates
    dates = re.findall(date_pattern, text)
    print("\n📅 Extracted Dates:")
    for date in dates:
        print("   ➤", date)

    with open("extracted_data.txt", "w", encoding="utf-8") as f:
        f.write("Extracted Emails:\n")
        for email in emails:
            f.write(f"📧 {email}\n")
        f.write("\nExtracted Phone Numbers:\n")
        for phone in phones:
            f.write(f"📱 {phone}\n")
        f.write("\nExtracted Dates:\n")
        for date in dates:
            f.write(f"📅 {date}\n")

print("Paste your paragraph (type DONE to finish):")
lines = []
while True:
    line = input()
    if line.strip().upper() == "DONE":
        break
    lines.append(line)

text = "\n".join(lines)
extractor(text)