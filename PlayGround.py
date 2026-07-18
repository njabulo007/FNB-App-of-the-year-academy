#name = input('Enter your name: ')
#surname = input('Enter your surname: ')
#name = name.strip()
#length = len(name)

#print(f'Welcome {name.upper()} {surname.upper()}!\n Your name has {length} characters. \n Your initials are {name[0].upper()}{surname[0].upper()}.\n Your first name is {name.title()}.\n Your last name is {surname.title()}')

player1 = {
    'name' : '',
    'job' : '',
    'age' : '',
    'city' : '' 
    }

playerName = input('Please enter your name: ')
player1['name'] = playerName

print(player1.get('name'))