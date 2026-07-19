High_score = 150

while True:
    user_input = input('Please enter your high score: ').lower()
    user_input = user_input.strip()
    if user_input == 'stop':
        break  
    if user_input.isdigit():
        
        user_input = int(user_input)
        if user_input < High_score: 
            print('Good try!, keep playing')
        elif user_input > High_score:
            print("Wow! That's a new High score!")
    
