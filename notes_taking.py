from datetime import datetime

print("Enter your notes (type DONE to stop):")
notes = []

while True:
    line = input()
    if line.strip().upper() == "DONE":
        break
    notes.append(line)

# Save notes to file
with open("note.txt", "w") as f:
    f.write(f"Notes saved on: {datetime.now()}\n\n")
    f.write("\n".join(notes))
print("✅ Your notes are saved to 'note.txt'.")

# Read and display notes from file
with open("note.txt", "r") as f:
    note = f.read()
print("\n📝 Your Notes:\n", note)
