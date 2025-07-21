import csv
import json

name = input("Enter your name: ")
email = input("Enter your E-mail: ")
feedback = input("Enter your feedback: ")

data = [name, email, feedback]

feedback_dict = {
    "Name":name,
    "Email":email,
    "Feedback":feedback
}

# Text File
with open("user_feedback.txt", "w") as f:
    f.write("Name     : " + name + "\n")
    f.write("Email    : " + email + "\n")
    f.write("Feedback : " + feedback + "\n")
    print("\nUser feedback saved to text file successfully")

with open("user_feedback.txt", "r") as f:
    user_feedback = f.read()
    print("\n📝 User Feedback from TXT file:\n--------------------------")
    print(user_feedback)

# CSV File
with open("user_feedback.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Email", "Feedback"])
    writer.writerow(data)
    print("User feedback saved to CSV file successfully")

with open("user_feedback.csv", "r") as f:
    user_feedback = csv.reader(f)
    print("\n📝 User Feedback from CSV file:\n--------------------------")
    for row in user_feedback:
        print(" | ".join(row))

# JSON file
with open("user_feedback.json", "w") as f:
    json.dump(feedback_dict, f, indent=4)
    print("User feedback saved to JSON file successfully")

with open("user_feedback.json", "r") as f:
    user_feedback = json.load(f)
    print("\n📝 User Feedback from JSON file:\n--------------------------")
    for key, value in user_feedback.items():
        print(f"{key}: {value}")

