name = input('Enter your name: ')
surname = input('Enter your surname: ')
password = input('Enter your password: ')

clean_password = password.strip()

password_hint = clean_password[0] + clean_password[-1] 

print(f'Hey, {name.title()} {surname.title()}! Your password hint is: It starts with "{password_hint[0].upper()}" and ends with "{password_hint[-1].upper()}".')