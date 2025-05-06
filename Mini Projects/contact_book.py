import json  # Import the json module for reading/writing JSON files
import os  # Import the os module to check if the file exists

# File name where contacts will be stored
CONTACTS_FILE = 'contacts.json'


# Function to load contacts from the JSON file
def load_contacts():
    # Check if the file exists before trying to read it
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            # Load and return the JSON data (contacts as a dictionary)
            return json.load(file)
    # If file does not exist, return an empty dictionary
    return {}


# Function to save contacts to the JSON file
def save_contacts(contacts):
    # Open the file in write mode and save the contacts dictionary as JSON
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)  # Pretty-print JSON with indentation


# Function to add a new contact
def add_contact(contacts):
    name = input("Enter name: ")  # Prompt user to enter contact name
    if name in contacts:
        print("Contact already exists.")  # Avoid duplicate contact names
        return
    phone = input("Enter phone number: ")  # Get phone number from user
    email = input("Enter email address: ")  # Get email address from user
    # Add new contact to the dictionary
    contacts[name] = {"phone": phone, "email": email}
    # Save updated contacts to file
    save_contacts(contacts)
    print("Contact added.")  # Inform the user


# Function to display all saved contacts in a table format
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")  # Handle case when contact list is empty
        return

    # Print the header
    print(f"{'Name'.ljust(20)} {'Phone'.ljust(15)} {'Email'}")
    print("-" * 55)

    # Print each contact in a formatted row
    for name, info in contacts.items():
        print(f"{name.ljust(20)} {info['phone'].ljust(15)} {info['email']}")


# Function to update an existing contact
def update_contact(contacts):
    name = input("Enter name to update: ")  # Ask user for contact name to update
    if name not in contacts:
        print("Contact not found.")  # Notify if contact does not exist
        return
    # Prompt for new phone and email, allow skipping fields by leaving blank
    phone = input("Enter new phone number (leave blank to keep current): ")
    email = input("Enter new email address (leave blank to keep current): ")
    # Update contact only if new values are provided
    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    # Save the updated contacts
    save_contacts(contacts)
    print("Contact updated.")


# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter name to delete: ")  # Get the name of the contact to delete
    if name in contacts:
        del contacts[name]  # Remove contact from dictionary
        save_contacts(contacts)  # Save changes to file
        print("Contact deleted.")
    else:
        print("Contact not found.")  # If name is not in contacts


# Main function to run the program loop
def main():
    contacts = load_contacts()  # Load existing contacts from file
    while True:
        # Display menu options
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")  # Get user choice

        # Call corresponding functions based on user input
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            update_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Try again.")  # Handle invalid menu choices


# This ensures the main function runs only when this script is executed directly
if __name__ == "__main__":
    main()
