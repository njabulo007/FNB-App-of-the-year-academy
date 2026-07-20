#• Store at least 5 students as a list of dictionaries: [{name, maths, english, science}, …]
#• Use a for loop to iterate over all students and calculate each student’s average
#• Apply the grade/status logic from Unit 5 inside the loop
#• Build a results list of dictionaries containing: name, average, grade, status
#• After the main loop, calculate: class average, highest mark, lowest mark
#• Display a formatted class report showing individual results and class statistics
#• Use a while loop to let the user search for a student by name after the report is shown

students = [
    {'name':'Bonolo', 'maths':75, 'english':87, 'science': 69 },
    {'name':'Sihle', 'maths':72, 'english':90, 'science': 78 },
    {'name':'Mandla', 'maths':92, 'english':94, 'science': 90 },
    {'name':'George', 'maths':86, 'english':89, 'science': 78 },
    {'name':'Amanda', 'maths':96, 'english':88, 'science': 94 }
]

for student in students:
    student_average = student['maths'] + student['english']+ student['science']
    if student_average >= 80 :
        learner_grade = 'A'
    elif student_average >= 70 and student_average <= 79:
        learner_grade = 'B'
    elif student_average >= 60 and student_average <= 69:
        learner_grade = 'C'
    elif student_average >= 50 and student_average <= 59:
        learner_grade = 'D'
    else:
        learner_grade = 'F' 

    if student_average >= 50:
        learner_status = "Pass"

    else:
        learner_status = 'Fail'

results_list = []

for student_results in students:
    results = {
        'name' : student_results['name'],
        'average' : student_average,
        'grade' : student_average,
        'status' : learner_status
    }
    results_list.append(results)
print(results_list[1])

# a function that produces a class suummary report for all students
def class_summary_report():
    return

# a funtion that takes student name and prints their report card.
def report_card(student_name):
    return

# a function iterate over all students and calculate each student’s average 
def average_iteration():
    return

learner_name = input('Please enter your name: ')
maths_marks = int(input('Enter your Maths marks: '))
science_marks = int(input('Enter your Science marks: '))
english_marks = int(input('Enter your English marks: '))

for student_average in students['maths', 'engish', 'science']:
    student_average = maths_marks + science_marks + english_marks // 3



overall_percentage = student_average // 3

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