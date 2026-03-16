contacts = {}

while True:
    print("\n== Contact Book Menu ==")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = int(input("Choose an option (1-6): "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        if name in contacts:
            print("Contact already exists")
        else:
            contacts[name] = {
                "phone": phone,
                "email": email,
                "address": address
            }
            print("Contact added successfully")

    elif choice == 2:
        if not contacts:
            print("No contacts found")
        else:
            for name, details in contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")

    elif choice == 3:
        search_name = input("Enter name to search: ")
        if search_name in contacts:
            d = contacts[search_name]
            print(f"Name: {search_name}, Phone: {d['phone']}, Email: {d['email']}, Address: {d['address']}")
        else:
            print("Contact not found")

    elif choice == 4:
        update_name = input("Enter name to update: ")
        if update_name in contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contacts[update_name] = {
                "phone": phone,
                "email": email,
                "address": address
            }
            print("Contact updated successfully")
        else:
            print("Contact not found")

    elif choice == 5:
        delete_name = input("Enter name to delete: ")
        if delete_name in contacts:
            del contacts[delete_name]
            print("Contact deleted successfully")
        else:
            print("Contact not found")

    elif choice == 6:
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice")
