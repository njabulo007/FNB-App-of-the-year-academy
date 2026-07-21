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

def grade_from_average(avg):
    if avg >= 80:
        return 'A'
    if avg >= 70:
        return 'B'
    if avg >= 60:
        return 'C'
    if avg >= 50:
        return 'D'
    return 'F'


results_list = []
highest_mark = -1
lowest_mark = float('inf')
class_total_averages = 0.0

for s in students:
    total = s['maths'] + s['english'] + s['science']
    average = total / 3
    grade = grade_from_average(average)
    status = 'Pass' if average >= 50 else 'Fail'
    results_list.append({'name': s['name'], 'average': round(average,2), 'grade': grade, 'status': status})
    class_total_averages += average

    # update highest and lowest individual subject marks
    for subject in ('maths', 'english', 'science'):
        mark = s[subject]
        if mark > highest_mark:
            highest_mark = mark
        if mark < lowest_mark:
            lowest_mark = mark

class_average = class_total_averages / len(students)

print('=' * 50)
print('Class Results')
print('=' * 50)
for r in results_list:
    print(f"{r['name']:<10} | Avg: {r['average']:>5} | Grade: {r['grade']} | Status: {r['status']}")

print('\nClass average (average of student averages):', round(class_average,2))
print('Highest individual mark in the class:', highest_mark)
print('Lowest individual mark in the class:', lowest_mark)
print('=' * 50)

def search_student():
    while True:
        name = input("\nEnter student name to search (or 'exit' to quit): ").strip()
        if name.lower() == 'exit':
            break
        found = [r for r in results_list if r['name'].lower() == name.lower()]
        if found:
            r = found[0]
            print(f"{r['name']}: Average={r['average']} Grade={r['grade']} Status={r['status']}")
        else:
            print('Student not found. Try again.')


if __name__ == '__main__':
    # Show the report and allow searching
    search_student()