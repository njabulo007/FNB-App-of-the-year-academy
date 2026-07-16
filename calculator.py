
#Wrap the calculator code in a try-except block to handle division by zero errors
try:
    first_number = float(input("Please enter the first number: "))
    second_number = float(input("Please enter the second number: "))

    #Perform basic arithmetic operations
    addition = first_number + second_number
    subtraction = first_number - second_number
    multiplication = first_number * second_number
    division = first_number / second_number
    exponentiation = first_number ** second_number

    print(f'Addition: {round(addition, 2)}')
    print(f'Subtraction: {round(subtraction, 2)}')
    print(f'Multiplication: {round(multiplication, 2)}')
    print(f'Division: {round(division, 2)}')
    print(f'Exponentiation: {round(exponentiation, 2)}')

    floor_division = first_number // second_number
    modulus = first_number % second_number

    print(f'Floor Division: {round(floor_division, 2)}')
    print(f'Modulus: {round(modulus, 2)}')

    #Absolute value tells you how far a number is from zero
    absolute_value = abs(first_number)
    print(f'Absolute Value: {round(absolute_value, 2)}')

#Handle division by zero error
except ZeroDivisionError:
    print("Cannot divide by zero.")