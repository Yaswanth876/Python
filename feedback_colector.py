name = input("Enter your name: ")
email = input("Enter your E-mail: ")
feedback = input("Enter your feedback: ")

# Writing formatted feedback to file
with open("user_feedback.txt", "w") as f:
    f.write("Name     : " + name + "\n")
    f.write("Email    : " + email + "\n")
    f.write("Feedback : " + feedback + "\n")

# Reading from file
try:
    with open("user_feedback.txt", "r") as f:
        user_feedback = f.read()
    print("\n📝 User Feedback Received:\n--------------------------")
    print(user_feedback)
except FileNotFoundError:
    print("❌ Oops! File not found. Please submit feedback first.")
