# Making Contact Book App

#features we have are
'''
1. Add a contact
2. View all contact
3. search a contact by name
4. Edit a contact
5. Exit
'''
import json
import os
# this loads the contact from current folder to python handle
def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json") as f:
            return json.load(f)
    return {}

# saving the contact
def save_contacts(contact):
    with open("contacts.json", "w") as f:
        json.dump(contact, f)


# showing the menu
def show_menu():
    print("\n----Contact Book----")
    print("1. Add a contact")     
    print("2. View a contact")
    print("3. Search a contact")
    print("4. Edit a contact")
    print("5. Exit ")

# adding the contact
def add_contact():
    global contact_book
    name=input("Enter the name: ")
    number=int(input("Enter the number: "))
    contact_book[name]=[number]
    save_contacts(contact_book)
    print("Contact Saved")


# Function for View the contacts:

def view_contact():
    contacts=load_contacts()
    if not contacts:
        print("No contact is found")
    else:
        for name, number in contacts.items():
            print(f"{name} :{', '.join(map(str, number))}")

# search function which searches contacts by name:

def search():
    contacts=load_contacts()
    name=input("Enter the name: ")
    name_lower=name.lower()
    contact_lower={key.lower(): value for key,value in contacts.items()}
    print(f"{name}: {contact_lower.get(name_lower, "Not exist")}")

# Editing the contacts details:
def edit():
    contacts=load_contacts()
    dec=int(input('''
Enter:
1. Edit Name
2. Edit Number
3. Exit
:-> '''))
    if dec==1:
        name=input("Enter the name: ")
        name_lower=name.lower()0
        contact_lower={key.lower(): value for key,value in contacts.items()}
        new_name=input("Enter the new name: ")
        contacts.values[name]=[new_name]
        #new_name=input("Enter the new name: ")

    if dec==3:
        exit()

#  Start of the code:-    
contact_book=load_contacts()

while True:
    show_menu()
    choice=int(input(" Enter your choice from 1 to 5: "))

    if choice == 1:
        add_contact()
    if choice == 2:
        view_contact()
    if choice == 3:
        search()
    if choice==4:
        edit()
    if choice==5:
        True

