#•	Collect learner name and marks for three subjects (as floats) using input()
#•	Calculate the average mark across the three subjects
#•	Assign a letter grade: A (80+), B (70-79), C (60-69), D (50-59), F (below 50) using if/elif/else
#•	Assign Pass status if the average is 50 or above, Fail otherwise
#•	Flag any individual subject mark below 40 as ‘needs intervention’
#•	Display a formatted report card showing all inputs, the average, the grade, the status, and any intervention flags


learner_name = input('Please enter your name: ')
maths_marks = int(input('Enter your Maths marks: '))
science_marks = int(input('Enter your Science marks: '))
english_marks = int(input('Enter your English marks: '))

average_mark = maths_marks + science_marks + english_marks // 3

if average_mark >= 80 :
    learner_grade = 'A'
elif average_mark >= 70 and average_mark <= 79:
    learner_grade = 'B'
elif average_mark >= 60 and average_mark <= 69:
    learner_grade = 'C'
elif average_mark >= 50 and average_mark <= 59:
    learner_grade = 'D'
else:
    learner_grade = 'F' 

if average_mark >= 50:
    learner_status = "Pass"

else:
    learner_status = 'Fail'

overall_percentage = average_mark // 3

print('``' * 20)
print(f"{learner_name.title()}'s report card")
print('``' * 20)

print(f' Hello {learner_name.title()}! see your marks below\n Maths: {maths_marks}\n Science: {science_marks}\n English: {english_marks}\n Overall percentage: {overall_percentage}\n Learner status: {learner_status}')

if maths_marks < 40:
    print(f'You received below {maths_marks} in Maths, subject needs intervention')
if science_marks < 40:
    print(f'You received below {science_marks} in Science, subject needs intervention')
if english_marks < 40:
    print(f'You received below {english_marks} in English, subject needs intervention')

print('``' * 20)