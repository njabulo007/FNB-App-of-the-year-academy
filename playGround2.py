contact_book =[
    {'name' : 'John', 'phone' : '083 345 5559', 'email' : 'john@gmail.com'}
]
user_search = input('Enter a name to search: ')
for contact_search in contact_book:
    if contact_search['name'] == user_search:
        print(f'Name: {contact_search["name"]}\nPhone: {contact_search["phone"]}\nEmail address: {contact_search["email"]}')
    elif contact_search != user_search:
        print('Name not available in contact book, try another name or add it to your contact book by pressing 1')