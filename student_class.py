class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.avg = 0

    def add_marks(self, subject, mark):
        self.marks[subject] = mark
        print(f"✅ Added: {subject} - {mark} marks")

    def calculate_avg(self):
        if self.marks:
            self.avg = sum(self.marks.values()) / len(self.marks)
        else:
            self.avg = 0
            print("⚠️ No marks to calculate average!")

    def general_report(self):
        print("\n📝 ------- Student Report -------")
        print(f"Student Name : {self.name}")
        print(f"Roll Number  : {self.roll_no}")
        print("Subject Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
        print(f"Mark Average : {round(self.avg, 2)}")
        print("-------------------------------")

name = input("Enter your name: ")
roll_no = input("Enter your roll number: ")
marks = {}

s1 = Student(name, roll_no, marks)

# Add all marks BEFORE calculating average
s1.add_marks("Maths", 100)
s1.add_marks("Physics", 94)
s1.add_marks("Chemistry", 93)
s1.add_marks("Computer Science", 100)

s1.calculate_avg()
s1.general_report()
