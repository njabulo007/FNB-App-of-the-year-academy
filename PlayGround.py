#name = input('Enter your name: ')
#surname = input('Enter your surname: ')
#name = name.strip()
#length = len(name)

#print(f'Welcome {name.upper()} {surname.upper()}!\n Your name has {length} characters. \n Your initials are {name[0].upper()}{surname[0].upper()}.\n Your first name is {name.title()}.\n Your last name is {surname.title()}')

#player1 = {
#    'name' : '',
#    'job' : '',
#    'age' : '',
#    'city' : '' 
#    }

#playerName = input('Please enter your name: ')
#player1['name'] = playerName

#print(player1.get('name'))



name = input('Please enter your name: ')
age = int(input('Please enter your age: '))

def introduce(name, age):
    if age >= 25:
        print(f'Welcome {name} your age is {age} we consider you old enough to use our product safely ')
    else:
        print(f'Sorry {name}, you dont meet the required age to use our product.')


introduce(name,age)

contact_book = [
    {'name': 'John', 'phone' : '012 445 8874', 'email': 'john@gmail.com'}  
]
  

#printing a value in a dictinary that is inside a list called contact_book [0] is the fist item in the list which is the 1st dictionary. ['name'] is the key and its value (output) is John
print(contact_book[0]['name'])

#inserting an item in the list you fist list the index of a list followed by the key you need added, then that is = the value of that key NB. = is used instead of :
contact_book[0]['age'] = '25'
print(contact_book[0]['age'])

#adding another dictionary  inside a list, you wrap it inside append() methond
contact_book.append({
    'name' : 'Cindy',
    'phone' : '082 915 8874',
    'email' : 'cindy@gmail.com'
})

print(contact_book[1]['phone'])

students = [
    {'name' : 'Alice', 'mark' : 80},
    {'name' : 'Bob', 'mark' : 65},
    {'name' : 'John', 'mark' : 92}
    ]

print(students[2]['mark'])
for studentNames in students:
    print(studentNames['name'])

for top_marks in students:
    if top_marks['mark'] > 70:
        print(top_marks['mark'])