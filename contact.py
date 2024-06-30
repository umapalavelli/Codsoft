contact_list = []


def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address: ")
    contact_list.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
    print(f"{name} has been added to the contact book.")


def view_contacts():
    print("\nContact List:")
    for contact in contact_list:
        print(f"Name: {contact['Name']}, Phone: {contact['Phone']}")
        
def search_contact():
    name = input("Enter the contact's name to search: ")
    for contact in contact_list:
        if contact['Name'] == name:
            print(f"Contact found: Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}, Address: {contact['Address']}")
            return
    print(f"{name} not found in the contact book.")


def update_contact():
    name = input("Enter the contact's name to update: ")
    for contact in contact_list:
        if contact['Name'] == name:
            phone = input("Enter the new phone number: ")
            email = input("Enter the new email address: ")
            address = input("Enter the new address: ")
            contact.update({"Phone": phone, "Email": email, "Address": address})
            print(f"{name}'s contact information has been updated.")
            return
    print(f"{name} not found in the contact book.")


def delete_contact():
    name = input("Enter the contact's name to delete: ")
    for contact in contact_list:
        if contact['Name'] == name:
            contact_list.remove(contact)
            print(f"{name} has been deleted from the contact book.")
            return
    print(f"{name} not found in the contact book.")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice =='4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting the contact book. Goodbye!")

        break
    else:
        print("Invalid choice. Please select 1, 2, 3, 4 , 5 or 6.")