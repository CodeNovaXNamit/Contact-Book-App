# Making Contact Book App

#features we have are
'''
1. Add a contact
2. View all contact
3. search a contact by name
4. Edit a contact
5. Exit
'''

def show_menu():
    print("\n----Contact Book----")
    print("1. Add a contact")     
    print("2. View a contact")
    print("3. Search a contact")
    print("4. Edit a contact")
    print("5. Exit ")

def add_contact():
    name=input("Enter the name: ")
    number=int("Enter the number: ")

    contact_book[name]=[number]


    

    
contact_book={}

while True:
    show_menu()
    choice=int(input(" Enter your choice from 1 to 5"))

    if choice == 1:
        add_contact


