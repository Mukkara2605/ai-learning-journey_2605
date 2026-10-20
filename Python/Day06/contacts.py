# Contact book (contacts.py): use a dictionary of name to phone number. Add 3 contacts, then ask for a name and print the number, or Not found if missing.
contacts = { "Alice": "123-456-7890","Bob": "234-567-8901","Charlie": "345-678-9012"}
name = input("Enter a name: ")
if name in contacts:
    print(f"{name}'s phone number is {contacts[name]}")
else:
    print("Not found")
    
