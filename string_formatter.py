# gathering user input and storing it in variables
name = input('Enter your name: ')
surname = input('Enter your surname: ')
bio = input('Enter a short bio about yourself: ')

# cleaning up the input and calculating the length of the bio
bio = bio.strip()
length = len(bio)

# formatting and displaying the output
username = name[0].lower() + surname.lower()
print(f'Hey {name.title()} {surname.title()}! Your username is: {username}\nYour bio is {length} characters long.\n your bio with the replacement is: {bio.replace("I am ", "i\'m ")}')

