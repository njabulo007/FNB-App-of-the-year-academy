
# Creating variables to store needed data for second phase
name = input('What is your name: ')
surname = input('What is your surname: ')
favourite_number = float(input('Enter your favourite number in decimal form: '))
age = int(input('How old are you: '))

# next phase is to use the stored data in formated string in a display table
print("=" * 25)
print('Student Profile')
print("=" * 25)
print(f'Welcome, {name.upper()} {surname.title()}\n Age: {age * 12} Months\n favourite number: {round(favourite_number, 2)}' )
print("=" * 25)

print(type(name), type(surname), type(favourite_number), type(age))