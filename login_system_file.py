user_name = input("Enter username: ")
password = input("Enter password: ")

with open("login_form.txt", "w") as f:
    f.write("Username: " + user_name + "\n")
    f.write("Password: " + password + "\n")
print("Login info saved to file")

with open("login_form.txt", "r") as f:
    login_info = f.read()
print("User Login information:" + "\n------------------")
print(login_info)