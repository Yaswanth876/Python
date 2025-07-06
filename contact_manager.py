contacts = []

while True:
    print("\n----Contact Manager----")
    print("1. Add contact")
    print("2. View All contacts")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts.append((name, phone))
        print("Contact added successfully!")

    elif choice == 2:
        if not contacts:
            print("\nNo contacts found")
        else:
            print("\n----All Contacts----")
            for name, phone in contacts:
                print(f"Name: {name}, Phone: {phone}")

    elif choice == 3:
        search_name = input("Enter name to search: ")
        found = False
        for name, phone in contacts:
            if name.lower() == search_name.lower():
                print(f"Found -> Name: {name}, Phone: {phone}")
                found = True
                break
        if not found:
            print("\nContact not found")

    elif choice == 4:
        search_name = input("Enter name to delete: ")
        found = False
        for name, phone in contacts:
            if name.lower() == search_name.lower():
                contacts.remove((name, phone))
                print("\nContact deleted successfully!")
                found = True
                break
        if not found:
            print("\nContact not found")

    elif choice == 5:
        print("\nExiting Contact Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Try again!")
