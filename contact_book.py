contact_book =[
    {'name' : 'John', 'phone' : '083 345 5559', 'email' : 'john@gmail.com'}
]

def add_contact():
    name = input('Please enter contact name: ') 
    phone = int(input('Please enter contact phone number: ') )
    email = input('Please enter contact Email address: ')
    contact_book.append(
        {'name' : name,
        'phone' : phone,
        'email' : email},
    print(f"You successfuly added {contact_book['name']}'s contact info")

    )

def search_name(name):
    for contact_search in contact_book:
        contact_search.get('name')
        if contact_search not in user_search:
            print('Not available')
        else:
            print(contact_search)

def delete_contact(name):
    
    for contact_delete in contact_book:
        contact_delete.get('name')
        if contact_delete not in user_delete:
            print('Not available')
        else:
                contact_book.pop(contact_delete)

def view_all():
    for contact in contact_book:
        print(f"{contact['name']}")

while True:
    user_select = int(input('press 1 to add - 2 to search - 3 to delete - 4 to view all contacts and 5 to exit: '))
    if user_select == 1:
        add_contact()
    elif user_select == 2:
        user_search = input('Enter a name to search: ')
        search_name(user_search)
    elif user_select == 3:
        user_delete = input('Enter the name of the contact you want to delete: ')
        delete_contact(user_delete)
    elif user_select == 4:
        view_all()
    elif exit == 5:
        break