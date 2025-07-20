class FeedbackCollector:
    def __init__(self, name, email, feedback):
        self.name = name
        self.email = email
        self.feedback = feedback
    def save_to_file(self):
        with open("user_feedback.txt", "w") as f:
            f.write("Name     : " + self.name + "\n")
            f.write("Email    : " + self.email + "\n")
            f.write("Feedback : " + self.feedback + "\n")
    def show_file_content(self):
        try:
            with open("user_feedback.txt", "r") as f:
                user_feedback = f.read()
            print("\n📝 User Feedback Received:\n--------------------------")
            print(user_feedback)
        except FileNotFoundError:
            print("❌ Oops! File not found. Please submit feedback first.")

name = input("Enter your name: ")
email = input("Enter your E-mail: ")
feedback = input("Enter your feedback: ")

feed = FeedbackCollector(name, email, feedback)
feed.save_to_file()
feed.show_file_content()
