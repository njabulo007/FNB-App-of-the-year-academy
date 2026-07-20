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