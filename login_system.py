user_name = input("Username: ")
count = 1
access = 0

while count <= 3:
    password = input(f"Attempt {count}/3 - Enter Password: ")
    if password == "Admin@123":
        print("Access Granted ✅")
        access = 1
        break
    else:
        print("Password incorrect! Try again...\n")
    count += 1

if not access:
    print("Access Denied 🚫")
