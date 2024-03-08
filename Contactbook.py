#contact book
import os
contacts = {}
def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    address = input("Enter the contact's address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print(f"{name} has been added to your contacts.")
def view_contact_list():
    print("Contact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")
def search_contact():
    query = input("Enter the name or phone number to search for a contact: ")
    results = []
    for name, details in contacts.items():
        if query in name or query in details['phone']:
            results.append((name, details))
    if results:
        print("Search results:")
        for name, details in results:
            print(f"Name: {name}, Phone: {details['phone']}")
    else:
        print("No matching contacts found.")
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Current Details for {name}:")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")
        choice = input("What do you want to update (phone/email/address)? ").lower()
        if choice == 'phone':
            contacts[name]['phone'] = input("Enter the new phone number: ")
        elif choice == 'email':
            contacts[name]['email'] = input("Enter the new email address: ")
        elif choice == 'address':
            contacts[name]['address'] = input("Enter the new address: ")
        else:
            print("Invalid choice.")
    else:
        print("Contact not found.")
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted from your contacts.")
    else:
        print("Contact not found.")
while True:
    print("\nThe Contact settings are:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")
with open('contacts.txt', 'w') as file:
    for name, details in contacts.items():
        file.write(f"{name},{details['phone']},{details['email']},{details['address']}\n")
print("Contact settings closed.")