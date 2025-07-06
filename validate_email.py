def validate_email(email):
    if "@" in email and "." in email and email == email.strip() and (email.endswith(".com") or email.endswith(".in")):
        return True
    else:
        return False

mail = input("Enter your E-mail: ")

if validate_email(mail):
    print("Valid E-mail")
else:
    print("Invalid E-mail!")
