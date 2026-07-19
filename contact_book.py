
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
        {'name' : name.title(),
        'phone' : phone,
        'email' : email.title()}
        )
    print(f"You successfuly added {contact_book[-1]['name']}'s contact info")
    
#a function that takes one argument > name and searches the inputed name and prints it
def search_name(name):
    for contact_search in contact_book:
        if contact_search['name'] == user_search:
            print('"' * 18)
            print(f'Name: {contact_search["name"]}\nPhone: {contact_search["phone"]}\nEmail address: {contact_search["email"]}')
            print('"' * 18)
        elif contact_search != user_search:
            print('Name not available in contact book, try another name or add it to your contact book by pressing 1')
        


#a function that that takes one argument > name and searches by looping through the list to find the name the user inputed and uses .pop() to remove that user name
def delete_contact(name):
    
    for contact_delete in contact_book:
        if contact_delete['name'] == user_delete:
            contact_book.remove(contact_delete)
            print(f"You successfully deleted {contact_delete['name']}'s contact " )
        elif contact_delete['name'] != user_delete:  
            print('Name not available in contact book, try another name or add it to your contact book by pressing 1')
                

#a function that takes no argument and loops through the list and searches for all names and prints them out
def view_all():
    for contact in contact_book:
        print(f" name: {contact['name']} --> phone: {contact['phone']} --> email: {contact['email']}")


# a while function to make sure code is always running for the user to be able to decide choise. the if and else if statements check user unput and runs the apropriate functions.
while True:
    try:
        user_select = int(input('press 1 to add - 2 to search - 3 to delete - 4 to view all contacts and 5 to exit: '))
        if user_select == 1:
            add_contact()
        elif user_select == 2:
            user_search = input('Enter a name to search: ').title()
            search_name(user_search)
        elif user_select == 3:
            user_delete = input('Enter the name of the contact you want to delete: ').title()
            delete_contact(user_delete)
        elif user_select == 4:
            view_all()
        elif user_select== 5:
            break
        elif user_select > 5:
            print('Enter a number between 1 and 5')
    except:
        print('Enter valid number')