#contact_book =[
#    {'name' : 'John', 'phone' : '083 345 5559', 'email' : 'john@gmail.com'}
#]
#user_search = input('Enter a name to search: ')
#for contact_search in contact_book:
#    if contact_search['name'] == user_search:
#        print(f'Name: {contact_search["name"]}\nPhone: {contact_search["phone"]}\nEmail address: {contact_search["email"]}')
#    elif contact_search != user_search:
#        print('Name not available in contact book, try another name or add it to your contact book by pressing 1')

students = [
    {'name':'Bonolo', 'maths':75, 'english':87, 'science': 69 },
    {'name':'Sihle', 'maths':32, 'english':20, 'science': 24 },
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

    print(student_average, learner_grade, learner_status)