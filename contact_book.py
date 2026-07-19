
#started with a list with one dictionary inside
contact_book =[
    {'name' : 'John', 'phone' : '083 345 5559', 'email' : 'john@gmail.com'}
]

# a function that adds contacts by appending user input inside the list of dictionary
def add_contact():
    name = input('Please enter contact name: ') 
    phone = int(input('Please enter contact phone number: ') )
    email = input('Please enter contact Email address: ')
    contact_book.append(
        {'name' : name,
        'phone' : phone,
        'email' : email}
        )
    print(f"You successfuly added {contact_book[-1]['name']}'s contact info")
#a function that takes one argument > name and searches the inputed name and prints it
def search_name(name):
    for contact_search in contact_book:
        contact_search.get('name')
        if contact_search == user_search:
            print(contact_search)
        elif contact_search != user_search:
            print('Name not available in contact book, try another name or add it to your contact book by pressing 1')
        


#a function that that takes one argument > name and searches by looping through the list to find the name the user inputed and uses .pop() to remove that user name
def delete_contact(name):
    
    for contact_delete in contact_book:
        contact_delete.get('name')
        if contact_delete != user_delete:
            print('Name not available in contact book, try another name or add it to your contact book by pressing 1')
        else:
                contact_book.pop(contact_delete)

#a function that takes no argument and loops through the list and searches for all names and prints them out
def view_all():
    for contact in contact_book:
        print(f" name: {contact['name']} --> phone: {contact['phone']} --> email: {contact['email']}")


# a while function to make sure code is always running for the user to be able to decide choise. the if and else if statements check user unput and runs the apropriate functions.
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
    elif user_select== 5:
        break
    else:
        print('Enter a valid option')