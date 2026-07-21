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
    {'name':'Amanda', 'maths':96, 'english':88, 'science': 94 },
    {'name':'Thandi', 'maths':82, 'english':85, 'science': 80 },
    {'name':'Tshepo', 'maths':60, 'english':62, 'science': 35 },
    {'name':'Nomsa', 'maths':90, 'english':93, 'science': 88 },
    {'name':'Bongi', 'maths':85, 'english':87, 'science': 82 },
    {'name':'Lerato', 'maths':70, 'english':75, 'science': 72 },
    {'name':'Sipho', 'maths':95, 'english':91, 'science': 93 },
    {'name':'Andile', 'maths':88, 'english':90, 'science': 86 }
]
highest_mark = 0
lowest_mark = 100
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
    if student["maths"] > highest_mark:
        highest_mark = student["maths"]
    if student["english"] > highest_mark:
        highest_mark = student["english"]           
    if student["science"] > highest_mark:
        highest_mark = student["science"]
    if student["maths"] < lowest_mark:
        lowest_mark = student["maths"]
    if student["english"] < lowest_mark:
        lowest_mark = student["english"]
    if student["science"] < lowest_mark:
        lowest_mark = student["science"]

print(f"highest_mark = {highest_mark}")
print(f"lowest_mark = {lowest_mark}")

results_list = []

# a for loop that iterates over all students and calculates each student’s average, grade and status
for student_results in students:
    results = {
        'name' : student_results['name'],
        'average' : student_average,
        'grade' : student_average,
        'status' : learner_status
    }
    results_list.append(results)


# a function that produces a class suummary report for all students
#def class_summary_report():
class_total = 0
for current_total in students:
    current_total = current_total['maths'] + current_total['english']+ current_total['science']
    class_total = class_total + current_total
    class_average = class_total / 12



    

print(class_total)
#return

# a funtion that takes student name and prints their report card.
def report_card(student_name):
    return

# a function iterate over all students and calculate each student’s average 
def average_iteration():
    return


