class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hi, I am {self.name}")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
p1 = Person(name, age)
p1.greet()