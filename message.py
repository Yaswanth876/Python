msg = input("Enter you message: ")

with open("msg.txt", "w") as f:
    f.write(msg)
print("Message is saved to file")

with open("msg.txt", "r") as f:
    content = f.read()
print("File Content:\n", content)