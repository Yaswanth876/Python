email = input("Enter your E-mail: ")

if "@" in email and "." in email and email == email.strip() and (email.endswith(".com") or email.endswith(".in")):
    print("Valid E-mail")
else:
    print("Invalid E-mail!!!")
